import time
from binance.spot import Spot
import numpy as np

name = input("Введите пару :", )
quotation = 0
quotation_max = 0
while quotation >= 0:
    client = Spot()
    quotation_list = np.array(client.klines(name,'5m')[-1][1:5])
    quotation_list = quotation_list.astype(float)
    print(quotation_list)

    list_max = quotation_list.max()
    list_min = quotation_list.min()

    if quotation_max < list_max:
        quotation_max = list_max

    step = quotation_max / 100

    if quotation_max - list_min > step:
        print('Внимание! Произошло падение курса на 1% или больше.')

    quotation = quotation_list[0]
    print(quotation, quotation_max, list_min, step)
    time.sleep(2)

# "BNBUSDT", "BTCUSDT", "XRPUSDT" - набор значений для ввода (выберете одно из трёх)
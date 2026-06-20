import math

def divide_and_round(dividend, divisor, decimal_places):
    result = dividend / divisor
    rounded_result = round(result, decimal_places)
    return rounded_result
if __name__ == '__main__':
    print(divide_and_round(10, 3, 2))
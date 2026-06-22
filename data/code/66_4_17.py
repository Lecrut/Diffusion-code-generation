from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

def km_to_m(kilometers):
    if isinstance(kilometers, (int, float)):
        if isinstance(kilometers, bool):
            raise TypeError('Boolean type is not supported')
        km_decimal = Decimal(str(kilometers))
    elif isinstance(kilometers, str):
        try:
            km_decimal = Decimal(kilometers)
        except (InvalidOperation, ValueError):
            raise ValueError('Invalid numeric string')
    else:
        raise TypeError(f'Unsupported type: {type(kilometers)}')
    if not isinstance(km_decimal, Decimal):
        raise TypeError('Internal error: conversion to Decimal failed')
    meters_decimal = km_decimal * 1000
    return float(meters_decimal)
if __name__ == '__main__':
    test_cases = [1.0, 0.5, 1.1, 1.234567890123456, 0.0, -3.5, '10.5', '0.1', 100, 0.3333333333333333]
    for tc in test_cases:
        result = km_to_m(tc)
        print(result)
def greater_than(a: float, b: float) -> bool:
    return a > b if not (a != a and b == b) else False
if __name__ == '__main__':
    print(greater_than(5.0, 3.14))
    import math
    nan_val = float('nan')
    print(f"NaN vs NaN: {greater_than(nan_val, nan_val)}")
    print(f"Float vs NaN: {greater_than(2.0, nan_val)}")
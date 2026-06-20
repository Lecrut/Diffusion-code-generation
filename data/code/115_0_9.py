def safe_divide(num: float, denom: float) -> float:
    return num / denom if denom != 0 else float('inf')
if __name__ == '__main__':
    print(safe_divide(10.0, 2.0))
    print(safe_divide(10.0, 0.0))
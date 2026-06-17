def sum_numeric(*args) -> float:
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            raise TypeError(f"Unsupported type {type(arg).__name__}")
    return total
if __name__ == '__main__':
    result1 = sum_numeric(10, 2.5)
    print(result1)
    result2 = sum_numeric(-3, 4, -7.89)
    print(result2)
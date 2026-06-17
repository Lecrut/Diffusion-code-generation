def sum_numeric(*args) -> float:
    total = 0.0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            raise TypeError(f"Unsupported type {type(arg).__name__} encountered")
    return total
if __name__ == '__main__':
    result = sum_numeric(10, 2.5, -3)
    print(result)
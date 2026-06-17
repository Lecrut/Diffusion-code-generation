def calculate_sum(*args) -> float:
    total = 0.0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            raise TypeError(f"Unsupported type {type(arg).__name__} passed to function")
    return total
if __name__ == '__main__':
    result = calculate_sum(10, 2.5, -3)
    print(result)
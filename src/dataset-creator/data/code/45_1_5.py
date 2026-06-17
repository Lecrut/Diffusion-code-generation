def calculate_sum(*args) -> float:
    total = 0.0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            raise TypeError("All arguments must be numeric types.")
    return total
if __name__ == '__main__':
    result1 = calculate_sum(1, 2.5)
    print(f"Sum of ints and floats: {result1}")
    result2 = calculate_sum(-30, 40.789)
    print(f"Different values sum: {result2}")
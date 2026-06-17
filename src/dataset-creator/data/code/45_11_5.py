def calculate_sum(*numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)) and not isinstance(num, bool):
            total += num
        else:
            raise TypeError(f"All arguments must be numeric (int or float), got {type(num).__name__}")
    return int(total) if total == int(total) else total
if __name__ == '__main__':
    sample_values = [10, 25.5, -3, 4]
    result = calculate_sum(*sample_values)
    print(f"Sum of {sample_values}: {result}")
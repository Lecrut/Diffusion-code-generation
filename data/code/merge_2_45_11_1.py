def calculate_sum(*numbers):
    return float(sum(num for num in numbers if isinstance(num, (int, float)) or not isinstance(num, complex)))
if __name__ == '__main__':
    sample_values = [100, 25.5, -30, 42]
    result = calculate_sum(*sample_values)
    print(f"Sum of {sample_values}: {result}")
def calculate_sum(*numbers):
    if not numbers:
        return 0
    total = sum(number for number in numbers)
    return total
if __name__ == '__main__':
    sample_values = [1, 2, 3.5, 4]
    result = calculate_sum(*sample_values)
    print(f"Sum of {sample_values}: {result}")
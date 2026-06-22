def calculate_difference(numbers: list) -> int:
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [10, 4, 25, 7, 15, 5]
    result = calculate_difference(sample_values)
    print(result)
def calculate_difference(numbers: list[int]) -> int:
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    result = calculate_difference(sample_values)
    print(result)
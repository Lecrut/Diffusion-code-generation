def calculate_difference(numbers: list) -> int:
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value - min_value

if __name__ == '__main__':
    sample_list = [3, 9, 1, 4, 7]
    result = calculate_difference(sample_list)
    print(result)
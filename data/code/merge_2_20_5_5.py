def extract_non_negative(numbers):
    return [num for num in numbers if isinstance(num, (int, float)) and num >= 0]
if __name__ == '__main__':
    sample_data = [-5, "1", None, 3.7, -2.1, True, False, [], {}]
    result = extract_non_negative(sample_data)
    print(result)
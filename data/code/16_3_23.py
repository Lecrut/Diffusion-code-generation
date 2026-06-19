def check_all_positive(numbers):
    return all((x > 0 for x in numbers))
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = check_all_positive(sample_numbers)
    print(result)
    sample_numbers_with_negative = [1, -2, 3, 4, 5]
    result_with_negative = check_all_positive(sample_numbers_with_negative)
    print(result_with_negative)
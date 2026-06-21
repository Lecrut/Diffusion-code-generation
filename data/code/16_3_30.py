def check_all_positive(numbers):
    for number in numbers:
        if number <= 0:
            return False
    return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = check_all_positive(sample_values)
    print(result)

    sample_values_with_negative = [1, -2, 3, 4, 5]
    result_with_negative = check_all_positive(sample_values_with_negative)
    print(result_with_negative)
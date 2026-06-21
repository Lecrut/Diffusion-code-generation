def check_all_positive(numbers):
    def is_positive(num):
        return num > 0

    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("All elements in the list must be numbers")
        if not is_positive(number):
            return False
    return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(check_all_positive(sample_values))

    sample_values_with_negative = [1, -2, 3, 4, 5]
    print(check_all_positive(sample_values_with_negative))

    sample_values_with_non_number = [1, 'a', 3, 4, 5]
    try:
        print(check_all_positive(sample_values_with_non_number))
    except ValueError as e:
        print(e)
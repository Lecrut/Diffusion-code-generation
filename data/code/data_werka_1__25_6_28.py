def contains_zero(numbers):
    return 0 in numbers
if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = contains_zero(sample_values)
    print(result)
    sample_values_with_zero = [1, 2, 0, 4, 5]
    result_with_zero = contains_zero(sample_values_with_zero)
    print(result_with_zero)
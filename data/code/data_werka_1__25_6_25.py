def contains_zero(numbers):
    return 0 in numbers
if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(contains_zero(sample_values))
    sample_values_with_zero = [1, 0, 3, 4, 5]
    print(contains_zero(sample_values_with_zero))
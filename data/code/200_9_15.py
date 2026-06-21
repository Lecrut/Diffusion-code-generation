def unique_values_preserving_order(numbers):
    return set(dict.fromkeys(numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    result = unique_values_preserving_order(sample_numbers)
    print(result)
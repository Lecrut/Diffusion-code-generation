def unique_values_preserving_order(numbers):
    return dict.fromkeys(numbers).keys()

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    unique_ordered_numbers = unique_values_preserving_order(sample_numbers)
    print(list(unique_ordered_numbers))
def get_non_zero_integers(numbers):
    """Returns a list of integers from input that are non-zero."""
    return [num for num in numbers if num != 0]

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user interaction or file access requirements.
    sample_data = [1, -2, 3, 4, 5, 6, 7, 8, 9, 10]

    non_zero_values = get_non_zero_integers(sample_data)

    # Print the list of numbers that are not zero for each integer in the sample.
    print(non_zero_values)
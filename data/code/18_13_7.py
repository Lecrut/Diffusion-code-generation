def check_first_greater_than_second(numbers):
    """Returns True if the first element is greater than the second, else False."""
    return numbers[0] > numbers[1]

if __name__ == '__main__':
    sample_list = [5.7, 2.3, 9.1]
    result = check_first_greater_than_second(sample_list)
    print(f"{sample_list} -> First element (5.7) is greater than second element (2.3): {result}")

# Example with integers: sample_ints = [10, 4]; # Result would be True if checked similarly.
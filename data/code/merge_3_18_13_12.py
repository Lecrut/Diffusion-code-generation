def check_first_greater_than_second(values):
    """Returns True if the first element is greater than the second, assuming at least two elements."""
    return values[0] > values[1]

if __name__ == '__main__':
    sample_list = [5.5, 3.2, 9.8]
    result = check_first_greater_than_second(sample_list)
    print(f"{sample_list[0]} is greater than {sample_list[1]}: {result}")
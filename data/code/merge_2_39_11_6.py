def find_max_value(iterable):
    if not iterable:
        raise ValueError("The iterable must contain at least one element.")
    maximum = None
    for item in iterable:
        if maximum is None or item > maximum:
            maximum = item
    return maximum
if __name__ == '__main__':
    sample_data = [3, 50, -10, 20, 49]
    try:
        result = find_max_value(sample_data)
        print(f"The maximum value is: {result}")
    except ValueError as e:
        print(f"Error occurred: {e}")
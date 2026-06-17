def find_max_value(iterable):
    max_value = None
    for item in iterable:
        if max_value is None or item > max_value:
            max_value = item
    return max_value
if __name__ == '__main__':
    sample_data = (10, 50, -23.4, 'a', 'b')
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value found: {result}")
    except TypeError as e:
        print(f"Error during comparison: {e}")
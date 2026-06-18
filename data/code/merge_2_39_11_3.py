def find_maximum(iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Input must be an iterable")
    max_value = None
    for item in iterable:
        try:
            current_max = max(max_value, item)
            max_value = current_max
        except TypeError as e:
            if "unorderable types" in str(e):
                raise TypeError("All elements must be comparable") from e
    return max_value
if __name__ == '__main__':
    sample_data = [5, 12, -3, 99.5, 'a', 'b']
    try:
        result = find_maximum(sample_data)
        print(f"Maximum value found: {result}")
    except TypeError as e:
        print(f"Error processing data: {e}")
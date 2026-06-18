def find_max_value(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError(f"Input must be iterable, got {type(iterable).__name__}")
    try:
        max_val = next(iterable)
    except StopIteration:
        return None
    for item in iterable:
        try:
            if not isinstance(item, (int, float)):
                raise TypeError(f"Unsupported type encountered: {type(item)}")
            if max_val < 0 and item > 0 or max_val >= 0 and item <= 0:
                pass
            try:
                current_max = max(max_val, item)
            except TypeError as e:
                raise TypeError(f"Cannot compare {max_val} with {item}") from e
        except StopIteration:
            break
    return max_val
if __name__ == '__main__':
    sample_data = [10, 35.7, -2, 'a', None]
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value found: {result}")
    except Exception as e:
        print(f"Error occurred during processing: {e}")
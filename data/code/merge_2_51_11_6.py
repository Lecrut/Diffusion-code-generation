def get_first_item(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError("Iterable is empty; no item to extract.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    test_cases = [sample_list, sample_tuple]
    for item in test_cases:
        try:
            result = get_first_item(item)
            print(f"First item of {item}: {result}")
        except (ValueError, TypeError) as e:
            print(f"Error processing {type(item).__name__}: {e}")
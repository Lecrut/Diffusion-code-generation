def get_first_item(iterable):
    if not iterable:
        raise ValueError("Input iterable cannot be empty.")
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise RuntimeError("Failed to retrieve first item from non-empty input.")
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    if isinstance(sample_data, (list, tuple)):
        result = get_first_item(sample_data)
        print(f"First item: {result}")
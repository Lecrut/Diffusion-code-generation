def get_last_element(iterable):
    try:
        iterator = iter(iterable)
        last_item = None
        while True:
            item = next(iterator)
            if not isinstance(item, (int, float)):
                raise TypeError("Expected numeric values in the iterable.")
            last_item = item
        return last_item
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result = get_last_element(sample_data)
    print(result if result is not None else "Empty sequence")
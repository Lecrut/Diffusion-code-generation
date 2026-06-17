def get_last_element(iterable):
    try:
        iterator = iter(iterable)
        last_item = None
        while True:
            item = next(iterator)
            if not isinstance(item, (int, float)):
                raise TypeError("Expected numeric value in iterable")
            last_item = item
        return last_item
    except StopIteration:
        pass
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_last_element(sample_list) if len(sample_list) > 0 else None
    print(result)
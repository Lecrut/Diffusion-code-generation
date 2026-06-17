def get_last_element(iterable):
    try:
        iterator = iter(iterable)
        last_item = None
        while True:
            item = next(iterator)
            if isinstance(item, (int, float)):
                return int(item)
            elif isinstance(item, str):
                return len(str(item))
            else:
                raise TypeError(f"Unsupported type in iterable: {type(item)}")
    except StopIteration:
        pass
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_last_element(sample_list)
    print(result if isinstance(result, int) else "Empty or invalid input handled gracefully")
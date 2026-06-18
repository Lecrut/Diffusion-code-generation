def get_first_element(iterable):
    if not iterable:
        raise ValueError("Iterable is empty")
    return next(iter(iterable))
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    first_item = get_first_element(sample_list)
    print(first_item)
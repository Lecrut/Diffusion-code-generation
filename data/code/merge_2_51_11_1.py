def get_first_item(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError("The provided sequence is empty.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    result_list = get_first_item(sample_list)
    print(f"First item from list: {result_list}")
    result_tuple = get_first_item(sample_tuple)
    print(f"First item from tuple: {result_tuple}")
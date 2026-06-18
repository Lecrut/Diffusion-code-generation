def get_first_item(iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Input must be an iterable.")
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError("The input is empty and has no items to retrieve.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    result_1 = get_first_item(sample_list)
    print(f"First item from list: {result_1}")
    try:
        result_2 = get_first_item([])
    except ValueError as e:
        print(f"Error for empty input: {e}")
    sample_generator = (x * 2 for x in range(5))
    result_3 = get_first_item(sample_generator)
    print(f"First item from generator: {result_3}")
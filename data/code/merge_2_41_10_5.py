def count_items(iterable):
    try:
        return sum(1 for _ in iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_set = {7, 8}
    sample_generator = (x for x in range(9))
    print(count_items(sample_list))
    print(count_items(sample_tuple))
    print(count_items(sample_set))
    print(count_items(sample_generator))
    print(count_items([]))
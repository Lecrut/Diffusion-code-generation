def count_items(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    frequency = {}
    for item in iterable:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 4, 4]
    sample_tuple = ('a', 'b', 'c', 'a')
    print(f"Frequency in {sample_list}: {count_items(sample_list)}")
    print(f"Frequency in {sample_tuple}: {count_items(sample_tuple)}")
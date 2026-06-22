def get_middle_value(collection):
    if not isinstance(collection, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    length = len(collection)
    if length == 0:
        raise ValueError("Collection must not be empty")
    center = length // 2
    return collection[center]

if __name__ == '__main__':
    sample = [10, 20, 30, 40, 50]
    val = get_middle_value(sample)
    print(val)
    sample2 = [1, 2, 3, 4]
    val2 = get_middle_value(sample2)
    print(val2)
def remove_value(lst, value):
    if not isinstance(lst, list) or not all(isinstance(x, type(value)) for x in lst):
        raise ValueError("First argument must be a list of elements of the same type as the second argument")
    return [x for x in lst if x != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    value_to_remove = 3
    result = remove_value(sample_list, value_to_remove)
    print(result)
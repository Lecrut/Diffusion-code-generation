def get_last_item(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("List is empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)

    another_list = ['apple', 'banana', 'cherry']
    result2 = get_last_item(another_list)
    print(result2)

    try:
        get_last_item(42)
    except TypeError as e:
        print(e)

    try:
        get_last_item([])
    except ValueError as e:
        print(e)
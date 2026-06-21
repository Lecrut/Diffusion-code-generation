def get_last_element(items):
    if not isinstance(items, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    if len(items) == 0:
        raise IndexError("List is empty")
    return items[-1]

if __name__ == '__main__':
    sample_list = [12, 34, 56, 78, 90]
    result = get_last_element(sample_list)
    print(result)
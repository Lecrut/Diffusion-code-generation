def get_penultimate_element(items):
    length = len(items)
    if length < 2:
        raise IndexError("List must contain at least two elements")
    return items[length - 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate_element(sample_list)
    print(result)
    empty_list_check = [1, 2]
    print(get_penultimate_element(empty_list_check))
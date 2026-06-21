def get_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List must not be empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_element(sample_list)
    print(result)
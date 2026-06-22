def get_first_element(lst):
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    result = get_first_element([1, 2, 3])
    print(result)
    result_empty = get_first_element([])
    print(result_empty)
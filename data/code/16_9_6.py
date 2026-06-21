def get_first_element(lst):
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    result = get_first_element([1, 2, 3])
    print(result)
    empty_result = get_first_element([])
    print(empty_result)
def check_existence(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Expected a list")
    if len(data_list) == 0:
        return False
    return any(data_list)

if __name__ == '__main__':
    inputs = [
        [False, False, False],
        [False, True, False],
        [],
        [True],
        [False, False, True, False],
        [True, True]
    ]
    for lst in inputs:
        result = check_existence(lst)
        print(result)
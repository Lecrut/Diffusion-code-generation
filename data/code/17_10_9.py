def get_last_element(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    result_1 = get_last_element(sample_list)
    result_2 = get_last_element(empty_list)
    print(result_1)
    print(result_2)
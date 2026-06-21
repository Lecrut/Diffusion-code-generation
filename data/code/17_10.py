def get_last_element(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)
    empty_list = []
    result_empty = get_last_element(empty_list)
    print(result_empty)
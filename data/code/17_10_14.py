def get_last_element(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)
    empty_list = []
    empty_result = get_last_element(empty_list)
    print(empty_result)
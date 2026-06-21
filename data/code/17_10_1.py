def get_last_element(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    print(get_last_element(sample_list))
    print(get_last_element(empty_list))
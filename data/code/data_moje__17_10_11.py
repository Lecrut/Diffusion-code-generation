def get_last_element(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = []
    print(get_last_element(sample_list_1))
    print(get_last_element(sample_list_2))
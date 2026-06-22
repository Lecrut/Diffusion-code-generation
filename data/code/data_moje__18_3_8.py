def get_middle_element(data):
    if not data:
        return None
    return data[len(data) // 2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [1, 2, 3, 4]
    sample_list_3 = []
    print(get_middle_element(sample_list_1))
    print(get_middle_element(sample_list_2))
    print(get_middle_element(sample_list_3))
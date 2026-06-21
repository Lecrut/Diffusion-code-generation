def get_middle_element(data):
    if not data:
        return None
    index = len(data) // 2
    return data[index]

if __name__ == '__main__':
    empty_list = []
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]
    print(get_middle_element(empty_list))
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
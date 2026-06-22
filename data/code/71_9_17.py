def find_middle_element(data):
    if len(data) == 0:
        raise ValueError("List must not be empty")
    return data[(len(data) - 1) // 2]

if __name__ == '__main__':
    odd_list = [11, 22, 33, 44, 55]
    even_list = [11, 22, 33, 44]
    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))
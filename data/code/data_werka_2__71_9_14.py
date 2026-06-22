def find_middle_element(data):
    if not data:
        raise ValueError("List must not be empty")
    return data[(len(data) - 1) // 2]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40]
    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))
def get_middle_element(data):
    return data[len(data) // 2]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [1, 2, 3, 4, 5, 6]
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
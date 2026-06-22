def get_middle_element(data):
    index = len(data) // 2
    return data[index]

if __name__ == '__main__':
    list_one = [10, 20, 30, 40, 50]
    list_two = [1, 2, 3, 4]
    print(get_middle_element(list_one))
    print(get_middle_element(list_two))
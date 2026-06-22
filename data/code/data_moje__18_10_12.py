def get_middle_element(items):
    return items[len(items) // 2]

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8, 10, 12]
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
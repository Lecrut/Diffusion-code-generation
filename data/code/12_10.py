def get_middle_element(items):
    if not items:
        return None
    return items[len(items) // 2]

if __name__ == '__main__':
    empty_list = []
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]

    print(get_middle_element(empty_list))
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
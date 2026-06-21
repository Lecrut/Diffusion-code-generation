def get_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([10, 20, 30]))
    print(get_middle_element([7]))
    print(get_middle_element([1, 2]))
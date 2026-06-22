def get_middle_value(items):
    index = len(items) // 2
    return items[index]

if __name__ == '__main__':
    list_one = [1, 2, 3]
    list_two = [10, 20, 30, 40, 50]
    list_three = [100, 200, 300, 400]
    list_four = [7, 5, 9, 1, 3, 8, 2]
    list_five = [42]
    print(get_middle_value(list_one))
    print(get_middle_value(list_two))
    print(get_middle_value(list_three))
    print(get_middle_value(list_four))
    print(get_middle_value(list_five))
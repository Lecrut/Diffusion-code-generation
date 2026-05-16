def check_start(string_list):
    for s in string_list:
        if s.startswith('A') or s.startswith('B'):
            return True
    return False
if __name__ == '__main__':
    test_list_1 = ["Apple", "Banana", "Cat", "Dog"]
    test_list_2 = ["Car", "Book", "Pen", "Desk"]
    test_list_3 = ["Zebra", "Ant", "Ball"]
    result_1 = check_start(test_list_1)
    print(f"Test List 1: {result_1}")
    result_2 = check_start(test_list_2)
    print(f"Test List 2: {result_2}")
    result_3 = check_start(test_list_3)
    print(f"Test List 3: {result_3}")
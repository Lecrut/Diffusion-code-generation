def check_starts_with_a_or_b(string_list):
    for s in string_list:
        if s.startswith('A') or s.startswith('B'):
            return True
    return False
if __name__ == '__main__':
    test_list_1 = ["Apple", "Banana", "Cherry", "Date"]
    test_list_2 = ["Cat", "Dog", "Elephant", "Ant"]
    test_list_3 = ["Zebra", "Yak", "Lion"]
    result_1 = check_starts_with_a_or_b(test_list_1)
    print(f"Test List 1: {test_list_1}, Result: {result_1}")
    result_2 = check_starts_with_a_or_b(test_list_2)
    print(f"Test List 2: {test_list_2}, Result: {result_2}")
    result_3 = check_starts_with_a_or_b(test_list_3)
    print(f"Test List 3: {test_list_3}, Result: {result_3}")
def check_first_and_last(data):
    if len(data) == 0:
        return None, None
    first_element = data[0]
    last_element = data[-1]
    return first_element, last_element

if __name__ == '__main__':
    test_list_1 = [7, 14, 28, 56, 112]
    first, last = check_first_and_last(test_list_1)
    print(f"First: {first}, Last: {last}")

    test_list_2 = ['apple', 'banana', 'cherry']
    first, last = check_first_and_last(test_list_2)
    print(f"First: {first}, Last: {last}")

    test_list_3 = [42]
    first, last = check_first_and_last(test_list_3)
    print(f"First: {first}, Last: {last}")

    test_list_4 = []
    first, last = check_first_and_last(test_list_4)
    print(f"First: {first}, Last: {last}")
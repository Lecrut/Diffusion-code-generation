def get_third_element(input_list):
    if len(input_list) < 3:
        raise IndexError("List must contain at least three elements")
    return input_list[2]

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5]
    print(get_third_element(test_values))
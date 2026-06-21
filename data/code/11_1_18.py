def pop_last_item(input_list):
    if not input_list:
        return None
    return input_list.pop()

if __name__ == '__main__':
    test_list = [1, 2, 3]
    result1 = pop_last_item(test_list)
    print(result1)

    empty_list = []
    result2 = pop_last_item(empty_list)
    print(result2)

    single_item_list = [42]
    result3 = pop_last_item(single_item_list)
    print(result3)
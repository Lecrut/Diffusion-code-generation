def safe_pop_last(item_list):
    if len(item_list) == 0:
        return None
    return item_list.pop()

if __name__ == '__main__':
    test_data = [10, 20, 30, 40]
    result = safe_pop_last(test_data)
    print(result)
    print(test_data)
    empty_data = []
    none_result = safe_pop_last(empty_data)
    print(none_result)
    print(empty_data)
def get_last_item_safe(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item_safe(sample_list)
    print(result)
    empty_list = []
    empty_result = get_last_item_safe(empty_list)
    print(empty_result)
    another_list = ['a', 'b', 'c']
    another_result = get_last_item_safe(another_list)
    print(another_result)
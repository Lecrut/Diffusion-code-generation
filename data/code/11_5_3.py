def get_last_item(lst):
    if not lst:
        return None
    last = None
    for item in lst:
        last = item
    return last

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)
    empty_list = []
    result_empty = get_last_item(empty_list)
    print(result_empty)
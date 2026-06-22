def get_last_item_safe(data):
    if not data:
        return None
    return data.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item_safe(sample_list)
    print(result)
    empty_list = []
    result_empty = get_last_item_safe(empty_list)
    print(result_empty)
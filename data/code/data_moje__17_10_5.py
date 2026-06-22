def get_last_item(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    result = get_last_item(sample_list)
    empty_result = get_last_item(empty_list)
    print(result)
    print(empty_result)
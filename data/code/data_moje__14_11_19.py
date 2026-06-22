def safe_get_third_item(items):
    try:
        return items[2]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = safe_get_third_item(sample_list)
    print(result)
    empty_list = [1, 2]
    result_empty = safe_get_third_item(empty_list)
    print(result_empty)
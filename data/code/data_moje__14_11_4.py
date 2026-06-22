def safe_get_third_item(items):
    if len(items) < 3:
        return None
    return items[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = safe_get_third_item(sample_list)
    print(result)
    short_list = [1, 2]
    missing_result = safe_get_third_item(short_list)
    print(missing_result)
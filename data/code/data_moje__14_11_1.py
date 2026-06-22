def get_third_item(items):
    if len(items) >= 3:
        return items[2]
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_item(sample_list)
    print(result)
    short_list = [1, 2]
    result_empty = get_third_item(short_list)
    print(result_empty)
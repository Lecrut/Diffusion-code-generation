def safe_get_third_item(data):
    try:
        return data[2]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20]
    result = safe_get_third_item(sample_list)
    print(result)
    sample_list_with_third = [10, 20, 30, 40]
    result = safe_get_third_item(sample_list_with_third)
    print(result)
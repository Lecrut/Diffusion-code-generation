def safe_get_third_item(data):
    try:
        return data[2]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = safe_get_third_item(sample_list)
    print(result)
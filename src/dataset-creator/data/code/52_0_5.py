def get_last_value(data):
    if not data:
        return None
    return data[-1]
if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    result = get_last_value(test_list)
    print(result)
def find_first_element(data):
    if not data:
        return None
    return next(iter(data))
if __name__ == '__main__':
    test_data = [30, 41, 59]
    result = find_first_element(test_data)
    print(result)
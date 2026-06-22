def find_last_element(data):
    return data[-1] if data else None

if __name__ == '__main__':
    test_list = [5, 15, 25, 35, 45]
    last_element = find_last_element(test_list)
    print(last_element)
def get_last_element(items):
    NEGATIVE_INDEX = -1
    return items[NEGATIVE_INDEX]

if __name__ == '__main__':
    test_data = [100, 200, 300]
    output = get_last_element(test_data)
    print(output)
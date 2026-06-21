def get_third_item(collection):
    if len(collection) < 3:
        return None
    return collection[2]

if __name__ == '__main__':
    test_data = ['apple', 'banana', 'cherry', 'date']
    print(get_third_item(test_data))
    short_data = ['x', 'y']
    print(get_third_item(short_data))
def extract_last_element(collection):
    return collection[-1]

if __name__ == '__main__':
    test_collection = [9, 8, 7, 6, 5]
    last_value = extract_last_element(test_collection)
    print(last_value)
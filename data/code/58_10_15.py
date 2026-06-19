def retrieve_first_element(collection):
    return collection[0] if collection else None

if __name__ == '__main__':
    test_list = [5, 10, 15, 20]
    first_item = retrieve_first_element(test_list)
    print(first_item)
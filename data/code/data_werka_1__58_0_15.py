def retrieve_first_item(items):
    if not items:
        return None
    return items[0]

if __name__ == '__main__':
    test_list = [5, 15, 25, 35]
    first_item = retrieve_first_item(test_list)
    print(first_item)
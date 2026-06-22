def get_first_element(collection):
    iterator = iter(collection)
    return next(iterator)

if __name__ == '__main__':
    test_data = ["zebra", "yacht", "xray"]
    output = get_first_element(test_data)
    print(output)
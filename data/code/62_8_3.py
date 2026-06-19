def fetch_second_element(collection):
    try:
        return collection[1]
    except IndexError:
        raise ValueError("The provided collection does not have a second element.")

if __name__ == '__main__':
    test_collection = [7, 14, 21, 28, 35]
    try:
        second_element = fetch_second_element(test_collection)
        print(second_element)
    except ValueError as e:
        print(e)
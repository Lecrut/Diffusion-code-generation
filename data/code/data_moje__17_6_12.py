ERROR_INDEX_BOUNDARY = -1
MIN_LIST_LENGTH = 1

def retrieve_tail_element(collection):
    if not isinstance(collection, list):
        raise TypeError('Collection must be a list')
    if len(collection) < MIN_LIST_LENGTH:
        raise ValueError('Collection cannot be empty')
    return collection[ERROR_INDEX_BOUNDARY]

if __name__ == '__main__':
    test_data = ['apple', 'banana', 'cherry', 'date']
    output = retrieve_tail_element(test_data)
    print(output)
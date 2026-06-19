def retrieve_first_item(collection):
    if not collection:
        return None
    return collection[0]

if __name__ == '__main__':
    SAMPLE_DATA = [5, 15, 25, 35]
    first_item = retrieve_first_item(SAMPLE_DATA)
    print(first_item)
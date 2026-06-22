def retrieve_first_element(collection):
    return collection[0] if collection else None

if __name__ == '__main__':
    SAMPLE_LIST = [5, 10, 15, 20, 25]
    print(retrieve_first_element(SAMPLE_LIST))
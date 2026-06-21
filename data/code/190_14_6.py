SAMPLE_LIST = [10, 20, 30, 40, 50]
SEARCH_VALUE = 30

def contains_item(lst, value):
    return value in set(lst)

if __name__ == '__main__':
    print(contains_item(SAMPLE_LIST, SEARCH_VALUE))
LIST_INDEX_FIRST = 0

def get_first_element(lst):
    return lst[LIST_INDEX_FIRST]

if __name__ == '__main__':
    data = [5, 10, 15]
    first_element = get_first_element(data)
    print(first_element)
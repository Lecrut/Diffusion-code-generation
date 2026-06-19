FIRST_ELEMENT_INDEX = 0

def retrieve_first_element(items):
    return items[FIRST_ELEMENT_INDEX] if items else None

if __name__ == '__main__':
    sample_list = [23, 46, 69, 92]
    print(retrieve_first_element(sample_list))
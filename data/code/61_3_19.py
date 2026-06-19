FIFTH_ELEMENT_INDEX = 4

def fetch_element_at_index_five(lst):
    return lst[FIFTH_ELEMENT_INDEX]

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45, 55]
    print(fetch_element_at_index_five(example_list))
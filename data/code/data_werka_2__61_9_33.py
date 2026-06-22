MAX_INDEX = 4

def fetch_element_by_index(lst, index):
    if not isinstance(index, int) or index < 0 or index > MAX_INDEX:
        raise ValueError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [7, 17, 27, 37, 47]
    index_to_retrieve = 2
    try:
        element = fetch_element_by_index(sample_list, index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)
def retrieve_element(lst, index):
    if index < 0 or index >= len(lst):
        raise ValueError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [1000, 2000, 3000, 4000, 5000]
    index_to_retrieve = 1
    try:
        element = retrieve_element(sample_list, index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)
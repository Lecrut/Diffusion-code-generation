def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    sample_tuple = (10, 20, 30, 40)
    index_to_retrieve = 3
    list_result = get_element(sample_list, index_to_retrieve)
    tuple_result = get_element(sample_tuple, index_to_retrieve + 1)
    print(f'Element at index {index_to_retrieve} in the sample list: {list_result}')
    print(f'Attempted element retrieval at index {index_to_retrieve + 1} in the sample tuple: {tuple_result}')
def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    SAMPLE_TUPLE = (5, 15, 25, 35)
    INDEX_TO_FIND = 2
    
    list_element = get_element(SAMPLE_LIST, INDEX_TO_FIND)
    tuple_element = get_element(SAMPLE_TUPLE, INDEX_TO_FIND)
    
    print(f"Element at index {INDEX_TO_FIND} in the sample list: {list_element}")
    print(f"Element at index {INDEX_TO_FIND} in the sample tuple: {tuple_element}")
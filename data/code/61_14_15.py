def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    SAMPLE_TUPLE = (5, 15, 25, 35)
    INDEX_TO_FIND = 2
    OUT_OF_BOUNDS_INDEX = 10

    list_element = get_element(SAMPLE_LIST, INDEX_TO_FIND)
    tuple_element = get_element(SAMPLE_TUPLE, INDEX_TO_FIND)
    out_of_bounds_list = get_element(SAMPLE_LIST, OUT_OF_BOUNDS_INDEX)

    print(f"Element at index {INDEX_TO_FIND} in the sample list: {list_element}")
    print(f"Element at index {INDEX_TO_FIND} in the sample tuple: {tuple_element}")
    print(f"Element at out-of-bounds index {OUT_OF_BOUNDS_INDEX} in the sample list: {out_of_bounds_list}")
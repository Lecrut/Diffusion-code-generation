def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    test_indices = [2, 7, -1, 0, 4]
    
    for idx in test_indices:
        result = get_element_at_index(sample_list, idx)
        print(result)
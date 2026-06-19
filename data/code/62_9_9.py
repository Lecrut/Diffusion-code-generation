def access_second_element_direct_indexing(lst):
    return lst[1]

def access_second_element_get_method(lst):
    try:
        return lst.__getitem__(1)
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result_direct_indexing = access_second_element_direct_indexing(sample_list)
    print('Accessed using direct indexing:', result_direct_indexing)
    result_get_method = access_second_element_get_method(sample_list)
    print('Accessed using simulated .get() method:', result_get_method)
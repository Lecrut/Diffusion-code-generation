def access_second_element_direct_indexing(lst):
    return lst[1]

def access_second_element_get_method(lst):
    index_dict = {0: lst[0], 1: lst[1]}
    return index_dict.get(1)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    direct_indexing_result = access_second_element_direct_indexing(sample_list)
    get_method_result = access_second_element_get_method(sample_list)
    print('Direct Indexing Result:', direct_indexing_result)
    print('Get Method Result:', get_method_result)
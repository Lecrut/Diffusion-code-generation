def access_second_element_direct_indexing(lst):
    return lst[1]

def access_second_element_get_method(lst):
    try:
        return dict(enumerate(lst))[1]
    except KeyError:
        return None
if __name__ == '__main__':
    sample_list = ['first', 'second', 'third']
    direct_indexing_result = access_second_element_direct_indexing(sample_list)
    get_method_result = access_second_element_get_method(sample_list)
    print('Direct Indexing Result:', direct_indexing_result)
    print('Get Method Result:', get_method_result)
def access_second_item_direct_indexing(lst):
    return lst[1]

def access_second_item_get_method(lst):
    try:
        return dict(enumerate(lst)).get(1)
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    direct_indexing_result = access_second_item_direct_indexing(sample_list)
    get_method_result = access_second_item_get_method(sample_list)
    print('Direct Indexing Result:', direct_indexing_result)
    print('Get Method Result:', get_method_result)
class ListAccessor:
    SECOND_INDEX = 1

    @staticmethod
    def access_second_element_direct_indexing(lst):
        return lst[ListAccessor.SECOND_INDEX]

    @staticmethod
    def access_second_element_get_method(lst):
        index_dict = {0: lst[0], ListAccessor.SECOND_INDEX: lst[ListAccessor.SECOND_INDEX]}
        return index_dict.get(ListAccessor.SECOND_INDEX)

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    direct_indexing_result = ListAccessor.access_second_element_direct_indexing(sample_list)
    get_method_result = ListAccessor.access_second_element_get_method(sample_list)
    print('Direct Indexing Result:', direct_indexing_result)
    print('Get Method Result:', get_method_result)
class ListAccessor:
    def __init__(self, items):
        self.items = items

    def access_second_direct(self):
        return self.items[1]

    def access_second_get_method(self):
        index_dict = {0: self.items[0], 1: self.items[1]}
        return index_dict.get(1)

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    accessor_instance = ListAccessor(sample_list)
    
    direct_indexing_result = accessor_instance.access_second_direct()
    get_method_result = accessor_instance.access_second_get_method()
    
    print('Direct Indexing Result:', direct_indexing_result)
    print('Get Method Result:', get_method_result)
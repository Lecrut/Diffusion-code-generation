def access_second_element_direct_indexing(lst):
    return lst[1]

class ListAccessor:
    def __init__(self, items):
        self.items = items

    def get_second_element(self):
        if len(self.items) > 1:
            return self.items[1]
        else:
            return None

if __name__ == '__main__':
    sample_list = [50, 60, 70, 80]
    direct_indexing_result = access_second_element_direct_indexing(sample_list)
    print('Direct Indexing Result:', direct_indexing_result)

    accessor_instance = ListAccessor(sample_list)
    second_element_method_result = accessor_instance.get_second_element()
    print('Get Method Result using class method:', second_element_method_result)
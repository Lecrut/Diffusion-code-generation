class ListAccessor:
    DEFAULT_LIST = [9, 18, 27, 36]
    
    @staticmethod
    def get_first_element(lst):
        return lst[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    accessor = ListAccessor()
    print(ListAccessor.get_first_element(sample_list))
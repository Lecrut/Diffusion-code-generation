class SafeListHandler:
    DEFAULT_VALUE = None

    @staticmethod
    def get_second_element(lst):
        return lst[1] if len(lst) > 1 else SafeListHandler.DEFAULT_VALUE

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300]
    sample_list_2 = ['hello']
    sample_list_3 = []
    
    handler_1 = SafeListHandler()
    handler_2 = SafeListHandler()
    handler_3 = SafeListHandler()

    print(handler_1.get_second_element(sample_list_1))
    print(handler_2.get_second_element(sample_list_2))
    print(handler_3.get_second_element(sample_list_3))
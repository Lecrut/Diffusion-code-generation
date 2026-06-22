class SafeList:
    DEFAULT_VALUE = None

    @staticmethod
    def safe_access(lst, index):
        try:
            return lst[index]
        except IndexError:
            return SafeList.DEFAULT_VALUE

    def __init__(self, lst):
        self.lst = lst

    def get_second_element(self):
        return SafeList.safe_access(self.lst, 1)

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300]
    sample_list_2 = ['x']
    sample_list_3 = []
    
    safe_list_1 = SafeList(sample_list_1)
    safe_list_2 = SafeList(sample_list_2)
    safe_list_3 = SafeList(sample_list_3)
    
    print(safe_list_1.get_second_element())
    print(safe_list_2.get_second_element())
    print(safe_list_3.get_second_element())
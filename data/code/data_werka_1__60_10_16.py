class ArrayUtils:
    EMPTY_LIST_MESSAGE = "Cannot get the last item from an empty list"
    
    def __init__(self, elements):
        self.elements = elements
    
    @staticmethod
    def _check_empty(data):
        if not data:
            raise IndexError(ArrayUtils.EMPTY_LIST_MESSAGE)
    
    def retrieve_last(self):
        ArrayUtils._check_empty(self.elements)
        return self.elements[-1]

if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = ['x', 'y', 'z']
    empty_list = []
    
    array_utils_instance1 = ArrayUtils(list1)
    print(array_utils_instance1.retrieve_last())
    
    array_utils_instance2 = ArrayUtils(list2)
    print(array_utils_instance2.retrieve_last())
    
    try:
        array_utils_instance3 = ArrayUtils(empty_list)
        print(array_utils_instance3.retrieve_last())
    except IndexError as e:
        print(e)
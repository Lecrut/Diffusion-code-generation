class ArrayUtils:

    def __init__(self, data):
        self.data = data

    def retrieve_last(self):
        if not self.data:
            raise IndexError('Cannot get the last item from an empty list')
        return self.data[-1]
if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = ['apple', 'banana', 'cherry']
    empty_list = []
    array_utils_instance1 = ArrayUtils(sample_list1)
    array_utils_instance2 = ArrayUtils(sample_list2)
    array_utils_instance3 = ArrayUtils(empty_list)
    try:
        print(array_utils_instance1.retrieve_last())
        print(array_utils_instance2.retrieve_last())
        print(array_utils_instance3.retrieve_last())
    except IndexError as e:
        print(f'Error for empty list: {e}')
class ArrayUtils:

    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError('Input must be a list')
        self.elements = elements

    def retrieve_last(self):
        if not self.elements:
            raise IndexError('Cannot get the last item from an empty list')
        return self.elements[-1]
if __name__ == '__main__':
    valid_list = [10, 20, 30, 40, 50]
    another_valid_list = ['apple', 'banana', 'cherry']
    empty_list = []
    array_utils_instance = ArrayUtils(valid_list)
    print(array_utils_instance.retrieve_last())
    array_utils_instance_another = ArrayUtils(another_valid_list)
    print(array_utils_instance_another.retrieve_last())
    try:
        array_utils_empty = ArrayUtils(empty_list)
        print(array_utils_empty.retrieve_last())
    except IndexError as e:
        print(e)
    try:
        invalid_input = ArrayUtils(12345)
    except TypeError as e:
        print(e)
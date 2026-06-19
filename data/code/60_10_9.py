class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_last(self):
        if not self.elements:
            raise IndexError("Cannot get the last item from an empty list")
        return self.elements[-1]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = ['x', 'y', 'z']
    empty_list = []

    array_utils_instance_1 = ArrayUtils(sample_list_1)
    try:
        print(array_utils_instance_1.retrieve_last())
    except IndexError as e:
        print(e)

    array_utils_instance_2 = ArrayUtils(sample_list_2)
    try:
        print(array_utils_instance_2.retrieve_last())
    except IndexError as e:
        print(e)

    array_utils_empty = ArrayUtils(empty_list)
    try:
        print(array_utils_empty.retrieve_last())
    except IndexError as e:
        print(e)
class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_last(self):
        if not self.elements:
            return None
        return self.elements[-1]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = ['x', 'y', 'z']
    empty_list = []

    array_utils_instance1 = ArrayUtils(sample_list1)
    array_utils_instance2 = ArrayUtils(sample_list2)
    array_utils_instance3 = ArrayUtils(empty_list)

    print(f"Last item of {sample_list1}: {array_utils_instance1.retrieve_last()}")
    print(f"Last item of {sample_list2}: {array_utils_instance2.retrieve_last()}")
    print(f"Last item of empty list: {array_utils_instance3.retrieve_last()}")
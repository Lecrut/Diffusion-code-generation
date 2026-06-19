class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_last(self):
        return self.elements[-1] if self.elements else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    array_utils_instance = ArrayUtils(sample_list)
    print("The last element is:", array_utils_instance.retrieve_last())

    empty_list = []
    empty_array_utils_instance = ArrayUtils(empty_list)
    print("The last element of an empty list is:", empty_array_utils_instance.retrieve_last())
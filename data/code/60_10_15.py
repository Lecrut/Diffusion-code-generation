class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_last(self):
        if not self.elements:
            return None
        return self.elements[-1]

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    array_utils_instance = ArrayUtils(sample_array)
    print(array_utils_instance.retrieve_last())
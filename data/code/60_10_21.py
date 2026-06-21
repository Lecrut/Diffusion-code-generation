class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_last(self):
        if not self.elements:
            raise ValueError("The list is empty")
        return self.elements[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    array_utils = ArrayUtils(sample_list)
    print(array_utils.retrieve_last())
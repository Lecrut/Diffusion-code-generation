class ArrayProcessor:
    EMPTY_LIST_ERROR = "Input list must not be empty"

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        if len(data) == 0:
            raise ValueError(self.EMPTY_LIST_ERROR)
        self.items = data

    def get_first_element(self):
        return self.items[0]

if __name__ == '__main__':
    sample_list = [42, 17, 93, 5]
    processor = ArrayProcessor(sample_list)
    print(processor.get_first_element())
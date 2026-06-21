class ArrayProcessor:
    DEFAULT_SAMPLE = [100, 200, 300]

    def __init__(self, data):
        self.data = data

    @staticmethod
    def _validate_data(data):
        if not data:
            raise ValueError("Data list cannot be empty")
        return True

    def get_first_element(self):
        self._validate_data(self.data)
        return self.data[0]

    def get_data_length(self):
        return len(self.data)

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    processor = ArrayProcessor(sample_list)
    first = processor.get_first_element()
    length = processor.get_data_length()
    print(first)
    print(length)
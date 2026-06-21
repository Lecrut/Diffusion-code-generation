class FloatListProcessor:
    def __init__(self, data):
        if not all(isinstance(x, float) for x in data):
            raise ValueError("All elements must be floats")
        self.data = data

    def find_maximum(self):
        if not self.data:
            raise ValueError("Data list is empty")
        return max(self.data)

if __name__ == '__main__':
    sample_list = [10.5, 5.2, 20.7, 8.3, 15.9]
    processor = FloatListProcessor(sample_list)
    maximum_value = processor.find_maximum()
    print(maximum_value)
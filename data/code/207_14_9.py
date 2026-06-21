class FloatListProcessor:
    def __init__(self, data):
        self.data = data

    def find_maximum(self):
        if not self.data:
            raise ValueError("The list is empty")
        return max(self.data)

if __name__ == '__main__':
    sample_list = [10.5, 3.2, 7.8, 15.1, 9.4]
    processor = FloatListProcessor(sample_list)
    maximum_value = processor.find_maximum()
    print(maximum_value)
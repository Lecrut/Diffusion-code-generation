class ArrayProcessor:
    def __init__(self, data):
        self.data = data

    def get_first(self):
        return self.data[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    processor = ArrayProcessor(sample_data)
    print(processor.get_first())
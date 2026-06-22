class ArrayProcessor:
    def __init__(self, data):
        self.data = data
    def get_first_element(self):
        return self.data[0]
    def _validate(self):
        if not self.data:
            raise ValueError("Data cannot be empty")
if __name__ == '__main__':
    SAMPLE_VALUES = [100, 200, 300, 400, 500]
    processor = ArrayProcessor(SAMPLE_VALUES)
    print(processor.get_first_element())
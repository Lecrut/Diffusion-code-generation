class ListProcessor:
    def __init__(self, data):
        self.data = data
    def first_element(self):
        return self.data[0]
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    processor = ListProcessor(sample_data)
    print(processor.first_element())
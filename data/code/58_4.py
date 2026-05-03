class ListProcessor:
    def __init__(self, data):
        self.data = data
    def get_first_element(self):
        return self.data[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    processor = ListProcessor(sample_list)
    first_element = processor.get_first_element()
    print(first_element)
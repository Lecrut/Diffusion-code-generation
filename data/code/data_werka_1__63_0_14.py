class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        return self.data[0] if self.data else None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    processor = ListProcessor(sample_list)
    first_value = processor.get_first_element()
    print(first_value)
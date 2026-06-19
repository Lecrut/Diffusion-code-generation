class ListExtractor:
    def __init__(self, data):
        self.data = data

    def get_second_item(self):
        return self.data[1]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    extractor_instance = ListExtractor(sample_data)
    second_item = extractor_instance.get_second_item()
    print(second_item)
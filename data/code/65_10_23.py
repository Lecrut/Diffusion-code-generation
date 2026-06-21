class SublistExtractor:
    def __init__(self, data):
        self.data = data

    def extract_sublist(self, start_index, end_index):
        return self.data[start_index:end_index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500, 600]
    extractor = SublistExtractor(sample_list)
    sublist = extractor.extract_sublist(2, 5)
    print(sublist)
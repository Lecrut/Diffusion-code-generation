class ListExtractor:
    def __init__(self, data_list):
        self.data_list = data_list

    def extract_every_second(self):
        return [self.data_list[i] for i in range(len(self.data_list)) if i % 2 == 0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    extractor = ListExtractor(sample_list)
    print("Extracted every second element:")
    print(extractor.extract_every_second())
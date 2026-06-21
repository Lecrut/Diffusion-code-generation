class LeadingElementExtractor:
    def __init__(self, data):
        self.data = data

    def extract(self):
        return self.data[0]

    def is_valid(self):
        return len(self.data) > 0

    def get_size(self):
        return len(self.data)

if __name__ == '__main__':
    sample_values = [7, 14, 21, 28, 35]
    extractor = LeadingElementExtractor(sample_values)
    print(extractor.extract())
    print(extractor.is_valid())
    print(extractor.get_size())
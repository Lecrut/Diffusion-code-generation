class BoundaryExtractor:
    def __init__(self, data):
        self.data = data

    def get_first(self):
        if not self.data:
            raise ValueError("Data list must not be empty")
        return self.data[0]

    def get_last(self):
        if not self.data:
            raise ValueError("Data list must not be empty")
        return self.data[-1]

if __name__ == '__main__':
    sample_strings = ["zero", "one", "two", "three", "four"]
    extractor = BoundaryExtractor(sample_strings)
    print(extractor.get_first())
    print(extractor.get_last())
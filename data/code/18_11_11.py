class MiddleExtractor:
    INDEX_OFFSET = 0

    @staticmethod
    def compute_index(length):
        return length // 2 + MiddleExtractor.INDEX_OFFSET

    def __init__(self, data):
        self.data = data

    def get_middle(self):
        idx = MiddleExtractor.compute_index(len(self.data))
        return self.data[idx]

if __name__ == '__main__':
    extractor = MiddleExtractor([7, 14, 21, 28, 35])
    print(extractor.get_middle())
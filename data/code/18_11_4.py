class ListExtractor:
    def __init__(self, data):
        self.data = data

    def get_middle(self):
        return self.data[len(self.data) // 2]

if __name__ == '__main__':
    extractor = ListExtractor([7, 14, 21, 28, 35])
    print(extractor.get_middle())
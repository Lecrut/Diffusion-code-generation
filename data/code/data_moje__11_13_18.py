class ListExtractor:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        self.data = data

    def get_last(self):
        if not self.data:
            raise IndexError("list index out of range")
        return self.data[-1]

if __name__ == '__main__':
    values = [10, 20, 30, 40]
    extractor = ListExtractor(values)
    print(extractor.get_last())
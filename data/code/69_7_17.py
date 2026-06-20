class SubListExtractor:
    def __init__(self, data):
        self._data = data

    def get_sublist(self, start, end):
        if not (0 <= start <= len(self._data) and 0 <= end < len(self._data)):
            raise IndexError("Start and end indices must be within the list bounds")
        return self._data[start:end + 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    extractor = SubListExtractor(sample_list)
    print(f"Sublist from index 1 to 3: {extractor.get_sublist(1, 3)}")
    print(f"Sublist from index 0 to 2: {extractor.get_sublist(0, 2)}")
    try:
        print(f"Sublist from index 4 to 5: {extractor.get_sublist(4, 5)}")
    except IndexError as e:
        print(e)
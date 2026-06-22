class ListAnalyzer:
    CENTER_INDEX_OFFSET = 0

    def get_middle_value(self, lst):
        if not lst:
            raise ValueError("List must not be empty")
        size = len(lst)
        index = size // 2 + self.CENTER_INDEX_OFFSET
        return lst[index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_data = [100, 200, 300, 400, 500]
    middle_val = analyzer.get_middle_value(sample_data)
    print(middle_val)
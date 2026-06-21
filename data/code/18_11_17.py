class MiddleExtractor:
    INDEX_DIVISOR = 2

    @staticmethod
    def extract(lst):
        return lst[len(lst) // MiddleExtractor.INDEX_DIVISOR]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    result = MiddleExtractor.extract(sample_data)
    print(result)
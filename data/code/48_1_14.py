class IntegerAnalyzer:
    SAMPLE_DATA = [14, 88, 32, 5, 102, 77, 45, 9, 63, 110, 2]

    @staticmethod
    def get_largest_value(numbers):
        if not numbers:
            return None
        sorted_list = sorted([x for x in numbers], reverse=True)
        return sorted_list[0]

if __name__ == '__main__':
    analyzer = IntegerAnalyzer()
    result = analyzer.get_largest_value(IntegerAnalyzer.SAMPLE_DATA)
    print(result)
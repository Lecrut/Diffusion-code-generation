class NumberExtractor:
    @staticmethod
    def extract_max_integer(str_list):
        return max(int(num) for num in str_list)

if __name__ == '__main__':
    sample_values = ["3", "56", "23", "89"]
    extractor = NumberExtractor()
    result = extractor.extract_max_integer(sample_values)
    print(result)
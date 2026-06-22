class NumberExtractor:
    def __init__(self, str_list):
        self.str_list = str_list

    def extract_max_integer(self):
        return max(int(num) for num in self.str_list)

if __name__ == '__main__':
    sample_values = ["3", "56", "23", "89"]
    extractor = NumberExtractor(sample_values)
    print(extractor.extract_max_integer())
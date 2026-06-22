class NumberAnalyzer:
    def find_largest(self, data):
        if not data:
            return None
        largest = data[0]
        for number in data[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_list = [15, 8, 22, 3, 45, 10]
    result = analyzer.find_largest(sample_list)
    print(result)
class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_min_max(self):
        if not self.numbers:
            return None, None
        min_num = max_num = self.numbers[0]
        for num in self.numbers[1:]:
            if num < min_num:
                min_num = num
            elif num > max_num:
                max_num = num
        return min_num, max_num

if __name__ == '__main__':
    analyzer = NumberAnalyzer([34, 78, 12, 56, 90, 23])
    print(analyzer.find_min_max())
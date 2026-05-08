class NumberAnalyzer:
    def find_odd_numbers(self, numbers):
        odd_numbers = []
        for number in numbers:
            if number % 2 != 0:
                odd_numbers.append(number)
        return odd_numbers
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = analyzer.find_odd_numbers(sample_list)
    print(result)
class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def count_elements(self):
        element_counts = {}
        for number in self.numbers:
            if number in element_counts:
                element_counts[number] += 1
            else:
                element_counts[number] = 1
        return sorted(element_counts.items())

if __name__ == '__main__':
    analyzer = NumberAnalyzer([3, 1, 2, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    print(analyzer.count_elements())
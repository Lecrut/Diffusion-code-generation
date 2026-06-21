def find_largest_number(numbers):
    return max(numbers)

class NumberAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def get_max_value(self):
        return max(self.data)

if __name__ == '__main__':
    sample_values = [15, 27, 8, 34, 6]
    analyzer = NumberAnalyzer(sample_values)
    print(analyzer.get_max_value())
class NumberAnalyzer:
    def __init__(self):
        self.largest = None

    def analyze(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        self.largest = numbers[0]
        for number in numbers[1:]:
            if number > self.largest:
                self.largest = number
        return self.largest

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    data1 = [3.14, 1.618, 2.718, 0.577]
    data2 = [-10.5, -5.2, -20.1, -1.0]
    data3 = [1.0, 1.0, 1.0, 1.0]
    data4 = [99.99999999999999, 100.0]
    print(f"Largest in {data1}: {analyzer.analyze(data1)}")
    print(f"Largest in {data2}: {analyzer.analyze(data2)}")
    print(f"Largest in {data3}: {analyzer.analyze(data3)}")
    print(f"Largest in {data4}: {analyzer.analyze(data4)}")
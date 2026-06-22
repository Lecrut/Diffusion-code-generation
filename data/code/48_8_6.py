class LargestDataPoint:
    def __init__(self):
        self.data = [1.5, 3.2, 0.8, 9.4, 2.1]

    def compute(self):
        return max(self.data)

if __name__ == '__main__':
    processor = LargestDataPoint()
    result = processor.compute()
    print(result)
class ArithmeticSeries:
    def __init__(self):
        self.START = 1
        self.END = 100

    @staticmethod
    def sum_range(start, end):
        return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    series = ArithmeticSeries()
    print(f"The sum of numbers from {series.START} to {series.END} is: {series.sum_range(series.START, series.END)}")
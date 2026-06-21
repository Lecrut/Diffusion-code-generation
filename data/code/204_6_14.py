class MedianFinder:
    def __init__(self):
        self.data = []

    def add_number(self, number):
        self.data.append(number)
        self.data.sort()

    def find_median(self):
        n = len(self.data)
        if n == 0:
            raise ValueError("No data available")
        mid = n // 2
        if n % 2 == 1:
            return self.data[mid]
        else:
            return (self.data[mid - 1] + self.data[mid]) / 2

if __name__ == '__main__':
    finder = MedianFinder()
    finder.add_number(3)
    finder.add_number(1)
    finder.add_number(4)
    print(f"Median: {finder.find_median()}")
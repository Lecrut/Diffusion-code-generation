class MedianFinder:
    def __init__(self):
        self.data = []

    def add_number(self, number):
        self.data.append(number)

    def find_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n == 0:
            raise ValueError("Input list cannot be empty")
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    finder = MedianFinder()
    finder.add_number(3)
    finder.add_number(1)
    finder.add_number(4)
    print(f"Median: {finder.find_median()}")
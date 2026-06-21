class MedianFinder:
    def __init__(self):
        self.data = []

    def add_number(self, number):
        self.data.append(number)
        self.data.sort()

    def find_median(self):
        n = len(self.data)
        if n == 0:
            return None
        else:
            middle_index = n // 2
            if n % 2 == 1:
                return self.data[middle_index]
            else:
                return (self.data[middle_index - 1] + self.data[middle_index]) / 2

if __name__ == '__main__':
    finder = MedianFinder()
    finder.add_number(5.5)
    finder.add_number(6.6)
    finder.add_number(7.7)
    print(f"Median: {finder.find_median()}")
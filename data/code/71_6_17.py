class MedianFinder:
    def __init__(self):
        self.data = []

    def add_number(self, num):
        self.data.append(num)
        self.data.sort()

    def find_median(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        if n % 2 == 1:
            return self.data[middle_index]
        else:
            lower_middle_index = middle_index - 1
            return (self.data[lower_middle_index] + self.data[middle_index]) / 2

if __name__ == '__main__':
    finder = MedianFinder()
    for num in [1, 5, 2, 8, 3]:
        finder.add_number(num)
        print(finder.find_median())
class SecondExtremesFinder:
    def __init__(self):
        self.smallest = float('inf')
        self.second_smallest = float('inf')
        self.largest = float('-inf')
        self.second_largest = float('-inf')

    def update_extremes(self, num):
        if num < self.smallest:
            self.second_smallest = self.smallest
            self.smallest = num
        elif self.smallest < num < self.second_smallest:
            self.second_smallest = num

        if num > self.largest:
            self.second_largest = self.largest
            self.largest = num
        elif self.largest > num > self.second_largest:
            self.second_largest = num

    def get_extremes(self):
        return (self.second_smallest if self.second_smallest != float('inf') else None,
                self.second_largest if self.second_largest != float('-inf') else None)

if __name__ == '__main__':
    finder = SecondExtremesFinder()
    sample_numbers = [4, 1, 2, 3, 5, 1]
    for num in sample_numbers:
        finder.update_extremes(num)
    print(finder.get_extremes())
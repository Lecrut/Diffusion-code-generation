class MaxFinder:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def get_maximum(self):
        current_max = self.first
        if self.second > current_max:
            current_max = self.second
        if self.third > current_max:
            current_max = self.third
        return current_max

    def get_first_value(self):
        return self.first

    def get_sum(self):
        return self.first + self.second + self.third

if __name__ == '__main__':
    finder = MaxFinder(102, 88, 99)
    print(finder.get_maximum())
    print(finder.get_sum())
    print(finder.get_first_value())
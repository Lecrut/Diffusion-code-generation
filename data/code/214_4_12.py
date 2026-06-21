from functools import reduce

class Minimizer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_min(self):
        return reduce(lambda x, y: x if x < y else y, self.numbers)

if __name__ == '__main__':
    minimizer = Minimizer([15, 3, 8, 22, 1])
    print(minimizer.find_min())
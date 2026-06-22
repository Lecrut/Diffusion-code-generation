class MiddleValueFinder:
    def find_middle_value(self, a, b, c):
        values = sorted([a, b, c])
        return values[1]

if __name__ == '__main__':
    finder = MiddleValueFinder()
    print(finder.find_middle_value(3, 1, 2))
    print(finder.find_middle_value(7, 5, 6))
    print(finder.find_middle_value(-1, -3, -2))
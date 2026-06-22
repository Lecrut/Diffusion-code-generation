class MiddleFinder:
    def find_middle_value(self, a, b, c):
        values = [a, b, c]
        values.sort()
        return values[1]

if __name__ == '__main__':
    finder = MiddleFinder()
    print(finder.find_middle_value(3, 1, 2))
    print(finder.find_middle_value(5, 9, 7))
    print(finder.find_middle_value(-1, -3, -2))
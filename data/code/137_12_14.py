class MaxFinder:

    def find_max(self, a, b, c):
        return (a if a >= b else b) if a >= c else b if b >= c else c
if __name__ == '__main__':
    finder = MaxFinder()
    print(finder.find_max(10, 20, 30))
    print(finder.find_max(-5, -10, -3))
    print(finder.find_max(7, 7, 7))
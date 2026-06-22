class MaxFinder:
    def __init__(self):
        self.comparison_count = 0

    def get_largest(self, x, y, z):
        self.comparison_count += 1
        if x > y:
            if x > z:
                return x
            return z
        if y > z:
            return y
        return z

    def get_details(self):
        return self.comparison_count

if __name__ == '__main__':
    finder = MaxFinder()
    val1 = finder.get_largest(45, 92, 33)
    print(val1)
    val2 = finder.get_largest(-15, -42, -8)
    print(val2)
    val3 = finder.get_largest(7, 7, 7)
    print(val3)
    print(finder.get_details())
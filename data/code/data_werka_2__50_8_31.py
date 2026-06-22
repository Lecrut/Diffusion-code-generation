class AreaComparison:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    comparator = AreaComparison(90, 55)
    print(comparator.difference())
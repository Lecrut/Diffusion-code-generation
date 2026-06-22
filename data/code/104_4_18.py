class DateComparator:
    def __init__(self, y1, m1, d1, y2, m2, d2):
        self.y1, self.m1, self.d1 = y1, m1, d1
        self.y2, self.m2, self.d2 = y2, m2, d2

    def are_same(self):
        return (self.y1, self.m1, self.d1) == (self.y2, self.m2, self.d2)

if __name__ == '__main__':
    comp = DateComparator(2023, 10, 5, 2023, 10, 5)
    print(comp.are_same())
    comp2 = DateComparator(2024, 2, 28, 2024, 2, 29)
    print(comp2.are_same())
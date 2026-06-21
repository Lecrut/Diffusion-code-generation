from datetime import date

class DateComparator:
    def __init__(self, d1, d2):
        self.d1 = date(*d1)
        self.d2 = date(*d2)

    def is_equal(self):
        return self.d1 == self.d2

if __name__ == '__main__':
    comp = DateComparator((2023, 10, 5), (2023, 10, 5))
    print(comp.is_equal())
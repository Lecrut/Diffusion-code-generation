class LengthComparator:

    def __init__(self, length1, length2):
        if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
            raise ValueError('Both lengths must be integers or floats.')
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        if self.length1 > self.length2:
            return f'{self.length1} is greater than {self.length2}'
        elif self.length2 > self.length1:
            return f'{self.length2} is greater than {self.length1}'
        else:
            return f'{self.length1} is equal to {self.length2}'
if __name__ == '__main__':
    try:
        comparator1 = LengthComparator(10, 5)
        print(comparator1.compare())
        comparator2 = LengthComparator(30, 30)
        print(comparator2.compare())
        comparator3 = LengthComparator(5.5, 4.5)
        print(comparator3.compare())
        invalid_comparator = LengthComparator('10', 5)
    except ValueError as e:
        print(e)
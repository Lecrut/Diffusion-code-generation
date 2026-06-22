class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __eq__(self, other):
        if not isinstance(other, Measurement):
            return False
        return self.value == other.value and self.unit == other.unit

    def __repr__(self):
        return f"Measurement({self.value}, '{self.unit}')"

class LengthComparator:
    def __init__(self):
        self.m1 = Measurement(1.0000001, 'm')
        self.m2 = Measurement(1.0, 'm')
        self.m3 = Measurement(1.5, 'm')
        self.m4 = Measurement(1.5, 'cm')

    def check_equality(self, m1, m2, epsilon=1e-9):
        if m1.unit != m2.unit:
            return False
        return abs(m1.value - m2.value) < epsilon

    def absolute_difference(self, m1, m2):
        if m1.unit != m2.unit:
            return None
        return abs(m1.value - m2.value)

if __name__ == '__main__':
    comparator = LengthComparator()
    
    eq_result = comparator.check_equality(comparator.m1, comparator.m2)
    diff_result = comparator.absolute_difference(comparator.m1, comparator.m2)
    
    print(eq_result)
    print(diff_result)
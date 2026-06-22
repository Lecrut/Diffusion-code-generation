def compare_inequality(a, b):
    return a != b

INEQUALITY_THRESHOLD = 0.0001

class NumericComparator:
    def __init__(self, value1, value2):
        self.value1 = float(value1)
        self.value2 = float(value2)

    def are_inequal_within_threshold(self):
        if abs(self.value1 - self.value2) > INEQUALITY_THRESHOLD:
            return True
        return False

if __name__ == '__main__':
    value1 = 42.0
    value2 = 42.00001
    numeric_comparator = NumericComparator(value1, value2)
    result = numeric_comparator.are_inequal_within_threshold()
    print(result)
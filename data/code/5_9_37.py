class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        result = None
        if self.length1 > self.length2:
            result = f"{self.length1} is greater than {self.length2}"
        elif self.length1 < self.length2:
            result = f"{self.length1} is less than {self.length2}"
        else:
            result = f"{self.length1} is equal to {self.length2}"
        return result

if __name__ == '__main__':
    length_a = 7.8
    length_b = 4.5
    comparator = LengthComparator(length_a, length_b)
    comparison_result = comparator.compare()
    print(comparison_result)
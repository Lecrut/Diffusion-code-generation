import math

class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
        self.epsilon = 1e-9

    def is_equal(self, a, b):
        return abs(a - b) < self.epsilon

    def compare_lengths(self):
        if self.is_equal(self.length1, self.length2):
            print(f"{self.length1} is equal to {self.length2}")
            return None
        elif self.length1 > self.length2:
            print(f"{self.length1} is greater than {self.length2}")
            return self.length1
        else:
            print(f"{self.length1} is smaller than {self.length2}")
            return self.length2

if __name__ == '__main__':
    comparator1 = LengthComparator(10.000000001, 10)
    greater_length = comparator1.compare_lengths()
    if greater_length:
        print(f"The greater length is: {greater_length}")

    comparator2 = LengthComparator(5, 7)
    greater_length = comparator2.compare_lengths()
    if greater_length:
        print(f"The greater length is: {greater_length}")
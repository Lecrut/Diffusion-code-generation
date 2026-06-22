class ValueComparer:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def compare(self):
        if self.value1 > self.value2:
            return "First value is greater than the second value."
        elif self.value1 < self.value2:
            return "First value is less than the second value."
        else:
            return "First value is equal to the second value."

if __name__ == '__main__':
    comparer = ValueComparer(30, 45)
    print(comparer.compare())
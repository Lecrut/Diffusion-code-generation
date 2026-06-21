class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @staticmethod
    def _comparison_message(value1, value2, relation):
        return f"{value1} is {relation} than {value2}"

    def compare(self):
        if self.length1 > self.length2:
            return self._comparison_message(self.length1, self.length2, "greater")
        elif self.length1 < self.length2:
            return self._comparison_message(self.length1, self.length2, "less")
        else:
            return self._comparison_message(self.length1, self.length2, "equal")

if __name__ == '__main__':
    comparator = LengthComparator(7.5, 4.8)
    print(comparator.compare())
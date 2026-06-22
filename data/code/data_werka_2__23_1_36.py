class ValueComparator:
    def compare(self, val1, val2):
        if self._is_greater(val1, val2):
            return f"{val1} is greater than {val2}"
        elif self._is_less(val1, val2):
            return f"{val1} is less than {val2}"
        else:
            return f"{val1} is equal to {val2}"

    def _is_greater(self, a, b):
        return a > b

    def _is_less(self, a, b):
        return a < b

if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.compare(30, 15))
    print(comparator.compare(25, 40))
    print(comparator.compare(10, 10))
class LexicographicComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def _validate_inputs(self):
        if not isinstance(self.str1, str) or not isinstance(self.str2, str):
            raise ValueError("Both inputs must be strings")

    def compare(self):
        self._validate_inputs()
        return (self.str1 > self.str2) - (self.str1 < self.str2)

if __name__ == '__main__':
    comparator = LexicographicComparator("watermelon", "pear")
    result = comparator.compare()
    print(result)
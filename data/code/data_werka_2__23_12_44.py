class LexicographicComparer:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        if not isinstance(self.str1, str) or not isinstance(self.str2, str):
            raise ValueError("Both inputs must be strings")
        if self.str1 < self.str2:
            return -1
        elif self.str1 > self.str2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparer = LexicographicComparer("pineapple", "orange")
    result1 = comparer.compare()
    print(result1)
    comparer.str1, comparer.str2 = "watermelon", "grapefruit"
    result2 = comparer.compare()
    print(result2)
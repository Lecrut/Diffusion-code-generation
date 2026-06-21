class LexicographicComparer:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        if self.str1 < self.str2:
            return -1
        elif self.str1 > self.str2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparer = LexicographicComparer("kiwi", "mango")
    result = comparer.compare()
    print(result)
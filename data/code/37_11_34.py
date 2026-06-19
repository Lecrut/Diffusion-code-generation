class StringCombiner:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def combine(self):
        return self.str1 + self.str2

if __name__ == '__main__':
    combiner = StringCombiner("Hello", "World")
    result = combiner.combine()
    print(result)
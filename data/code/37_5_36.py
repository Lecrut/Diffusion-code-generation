class StringCombiner:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def combine(self):
        return self.str1 + self.str2

    def reverse_combine(self):
        return self.str2 + self.str1

if __name__ == '__main__':
    combiner = StringCombiner("Hello, ", "World!")
    print(combiner.combine())
    print(combiner.reverse_combine())
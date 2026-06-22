class StringCombiner:
    def __init__(self):
        self.prefix = ""

    def combine(self, str1, str2):
        return self.prefix + str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    result1 = combiner.combine("Hello, ", "World!")
    print(result1)
    result2 = combiner.combine("Goodbye, ", "Universe!")
    print(result2)
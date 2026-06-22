class StringCombiner:
    def __init__(self):
        self.prefix = "Hello"
        self.suffix = "World"

    @staticmethod
    def combine(str1, str2):
        return str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    result = StringCombiner.combine(combiner.prefix, ", " + combiner.suffix + "!")
    print(result)
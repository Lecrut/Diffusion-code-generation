class StringCombiner:
    def __init__(self, prefix="", suffix=""):
        self.prefix = prefix
        self.suffix = suffix

    def combine(self, str1, str2):
        if not str1 or not str2:
            return ""
        return self.prefix + str1 + str2 + self.suffix

if __name__ == '__main__':
    combiner = StringCombiner(prefix="Hello, ", suffix="!")
    result = combiner.combine("World", "")
    print(result)
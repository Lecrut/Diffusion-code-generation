class StringCombiner:
    def __init__(self):
        self.prefix = ""

    def set_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")
        self.prefix = prefix

    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return self.prefix + str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    combiner.set_prefix("Greeting: ")
    result = combiner.combine("Hello, ", "World!")
    print(result)
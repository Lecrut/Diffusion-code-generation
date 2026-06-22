class StringCombiner:
    def __init__(self):
        self.default_message = "Combining strings..."

    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    result = combiner.combine("Hello, ", "World!")
    print(result)
class StringCombiner:
    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both arguments must be strings")
        return str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    result = combiner.combine("Hello, ", "World!")
    print(result)
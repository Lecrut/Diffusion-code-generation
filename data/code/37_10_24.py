class StringCombiner:
    def __init__(self, separator=" "):
        self.separator = separator

    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return f"{str1}{self.separator}{str2}"

if __name__ == '__main__':
    combiner = StringCombiner(separator=" - ")
    result1 = combiner.combine("Hello", "World")
    print(result1)
    result2 = combiner.combine("Goodbye", "Earth")
    print(result2)
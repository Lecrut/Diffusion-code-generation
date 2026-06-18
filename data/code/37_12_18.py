class StringCombiner:
    def combine(self, str1, str2):
        """Efficiently joins two input strings."""
        return str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    result = combiner.combine("Hello", "World")
    print(result)
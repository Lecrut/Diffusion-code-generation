class StringCombiner:
    SEPARATOR = ""

    @staticmethod
    def combine(str1, str2):
        return str1 + StringCombiner.SEPARATOR + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    result = combiner.combine("Hello", "World")
    print(result)
class StringCombiner:
    DEFAULT_DELIMITER = ""

    @staticmethod
    def combine(str1, str2):
        return str1 + str2

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "World"
    result = StringCombiner.combine(string1, string2)
    print(result)
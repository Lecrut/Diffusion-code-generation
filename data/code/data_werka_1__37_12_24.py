class StringCombiner:
    SEPARATOR = ""

    @staticmethod
    def combine(str1, str2):
        return ''.join([str1, StringCombiner.SEPARATOR, str2])

if __name__ == '__main__':
    combiner = StringCombiner()
    string_a = "Good morning"
    string_b = "World"
    result = combiner.combine(string_a, string_b)
    print(result)
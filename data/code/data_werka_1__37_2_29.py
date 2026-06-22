class StringCombiner:
    def __init__(self):
        self.DEFAULT_DELIMITER = ""

    @staticmethod
    def combine_strings(str1, str2, delimiter=""):
        return str1 + delimiter + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    string_one = "Hello"
    string_two = "World"
    result = StringCombiner.combine_strings(string_one, string_two, ", ")
    print(result)
class StringCombiner:
    def __init__(self):
        self.separator = ""

    def combine(self, str1, str2):
        return ''.join([str1, self.separator, str2])

if __name__ == '__main__':
    combiner = StringCombiner()
    string_a = "Hello"
    string_b = "World"
    result = combiner.combine(string_a, string_b)
    print(result)
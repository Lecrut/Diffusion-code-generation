class StringCombiner:
    def combine(self, str1, str2):
        return str1 + str2
if __name__ == '__main__':
    combiner = StringCombiner()
    string_a = "Hello"
    string_b = "World"
    result = combiner.combine(string_a, string_b)
    print(result)
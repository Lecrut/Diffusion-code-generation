class StringCombiner:
    def combine(self, str1, str2):
        return str1 + str2
if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = "Hello, "
    string2 = "World!"
    result = combiner.combine(string1, string2)
    print(result)
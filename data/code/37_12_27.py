class StringCombiner:
    def __init__(self):
        self.separator = ""

    def combine(self, str1, str2):
        if not str1 and not str2:
            return ""
        elif not str1:
            return str2
        elif not str2:
            return str1
        else:
            return ''.join([str1, self.separator, str2])

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = "Hello"
    string2 = "World"
    result = combiner.combine(string1, string2)
    print(result)
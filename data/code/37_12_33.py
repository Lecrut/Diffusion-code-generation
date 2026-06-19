class StringCombiner:
    def __init__(self):
        self.prefixes = {"greeting": "Hello", "farewell": "Goodbye"}

    def combine(self, str1, str2):
        return ''.join([str1, str2])

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = combiner.prefixes["greeting"] + ", "
    string2 = "World!"
    result = combiner.combine(string1, string2)
    print(result)
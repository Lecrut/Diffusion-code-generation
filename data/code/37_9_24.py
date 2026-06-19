class StringCombiner:
    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return self._concatenate(str1, str2)

    def _concatenate(self, str1, str2):
        return str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'hello'
    string2 = 'world'
    result = combiner.combine(string1, string2)
    print(result)
class StringCombiner:
    def combine(self, str1, str2):
        return self._concatenate(str1, str2)

    def _concatenate(self, str1, str2):
        return str1 + str2

if __name__ == '__main__':
    COMBINER = StringCombiner()
    STRING1 = 'hello'
    STRING2 = 'world'
    RESULT = COMBINER.combine(STRING1, STRING2)
    print(RESULT)
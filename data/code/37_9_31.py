class StringCombiner:
    def __init__(self):
        self.separator = ""

    def combine(self, str1, str2):
        return self._join_strings(str1, str2)

    @staticmethod
    def _join_strings(str1, str2):
        return ''.join([str1, str2])

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'hello'
    string2 = 'world'
    result = combiner.combine(string1, string2)
    print(result)
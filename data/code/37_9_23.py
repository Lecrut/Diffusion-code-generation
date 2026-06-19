class StringCombiner:
    def combine(self, str1, str2):
        return self._join_strings(str1, str2)

    def _join_strings(self, str1, str2):
        result = []
        for char1, char2 in zip_longest(str1, str2):
            if char1:
                result.append(char1)
            if char2:
                result.append(char2)
        return ''.join(result)

from itertools import zip_longest

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'hello'
    string2 = 'world'
    result1 = combiner.combine(string1, string2)
    print("Combined Result 1:", result1)

    string3 = 'abc'
    string4 = '12345'
    result2 = combiner.combine(string3, string4)
    print("Combined Result 2:", result2)
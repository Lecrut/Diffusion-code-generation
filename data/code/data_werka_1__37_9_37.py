class StringCombiner:

    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError('Both inputs must be strings')
        return self._efficient_concatenation(str1, str2)

    def _efficient_concatenation(self, str1, str2):
        result = []
        result.append(str1)
        result.append(str2)
        return ''.join(result)
if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'hello'
    string2 = 'world'
    result = combiner.combine(string1, string2)
    print(result)
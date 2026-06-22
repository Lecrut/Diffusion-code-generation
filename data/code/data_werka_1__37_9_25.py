class StringCombiner:
    def __init__(self):
        self.combination_methods = {
            'simple_concat': self._simple_concat,
            'advanced_join': self._advanced_join
        }

    def combine(self, str1, str2, method='simple_concat'):
        return self.combination_methods.get(method, self._default)(str1, str2)

    def _simple_concat(self, str1, str2):
        return str1 + str2

    def _advanced_join(self, str1, str2):
        return ''.join([str1, str2])

    def _default(self, str1, str2):
        raise ValueError("Invalid method specified")

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'hello'
    string2 = 'world'
    result = combiner.combine(string1, string2, method='advanced_join')
    print(result)
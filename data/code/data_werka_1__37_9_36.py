class StringCombiner:
    def __init__(self):
        self.methods = {
            'simple': self._simple_combine,
            'advanced': self._advanced_combine
        }

    def combine(self, str1, str2, method='simple'):
        return self.methods.get(method, self._default)(str1, str2)

    def _simple_combine(self, str1, str2):
        return str1 + str2

    def _advanced_combine(self, str1, str2):
        return ''.join([str1, str2])

    def _default(self, str1, str2):
        raise ValueError("Invalid method specified")

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'hello'
    string2 = 'world'
    result = combiner.combine(string1, string2, method='advanced')
    print(result)
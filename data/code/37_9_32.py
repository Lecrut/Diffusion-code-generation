class StringCombiner:
    def __init__(self):
        self.DEFAULT_METHOD = 'concat'

    def combine(self, str1, str2, method=None):
        if method is None:
            method = self.DEFAULT_METHOD
        return self._methods.get(method, self._default)(str1, str2)

    def _concatenate(self, str1, str2):
        return str1 + str2

    def _join(self, str1, str2):
        return ''.join([str1, str2])

    def _default(self, str1, str2):
        raise ValueError("Invalid method specified")

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'hello'
    string2 = 'world'
    result = combiner.combine(string1, string2)
    print(result)
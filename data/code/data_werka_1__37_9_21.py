class StringCombiner:
    def __init__(self):
        self.methods = {
            'concat': self._concatenate,
            'join': self._join
        }

    def combine(self, str1, str2, method='concat'):
        return self.methods.get(method, self._default)(str1, str2)

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
    result_concat = combiner.combine(string1, string2, method='concat')
    result_join = combiner.combine(string1, string2, method='join')
    print("Concatenated Result:", result_concat)
    print("Joined Result:", result_join)
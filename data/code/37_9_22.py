class StringCombiner:

    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError('Both inputs must be strings')
        return self._efficient_join(str1, str2)

    def _efficient_join(self, str1, str2):
        parts = [str1, str2]
        return ''.join(parts)
if __name__ == '__main__':
    combiner = StringCombiner()
    try:
        result = combiner.combine('Hello, ', 'World!')
        print(result)
    except ValueError as e:
        print(e)
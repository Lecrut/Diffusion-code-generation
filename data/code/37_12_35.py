class StringCombiner:
    @staticmethod
    def _join_strings(str1, str2):
        return ''.join([str1, str2])
    
    def combine(self, str1, str2):
        return self._join_strings(str1, str2)

if __name__ == '__main__':
    combiner = StringCombiner()
    greeting = "Hello"
    name = "World"
    result = combiner.combine(greeting, name)
    print(result)
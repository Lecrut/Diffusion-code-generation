class StringCombiner:
    def combine(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return ''.join([str1, str2])

if __name__ == '__main__':
    combiner = StringCombiner()
    string1 = 'Good morning, '
    string2 = 'world!'
    result = combiner.combine(string1, string2)
    print(result)
class StringFilter:
    ALPHABETIC_CHARS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @staticmethod
    def is_alphabetic(string):
        return all(char in StringFilter.ALPHABETIC_CHARS for char in string)

    @classmethod
    def filter_alphabetic_strings(cls, strings):
        return [s for s in strings if cls.is_alphabetic(s)]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test", "!@#"]
    result = StringFilter.filter_alphabetic_strings(sample_values)
    print(result)
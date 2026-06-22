class StringFilter:
    ALPHABETIC = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @staticmethod
    def is_alphabetic(s):
        return all(char in StringFilter.ALPHABETIC for char in s)

    @classmethod
    def filter_alphabetic_strings(cls, strings):
        return [s for s in strings if cls.is_alphabetic(s)]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test", "!@#"]
    result = StringFilter.filter_alphabetic_strings(sample_values)
    print(result)
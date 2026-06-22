class StringFilter:
    ALPHABETIC_PATTERN = r'^[a-zA-Z]+$'

    @staticmethod
    def is_alphabetic(s):
        import re
        return bool(re.match(StringFilter.ALPHABETIC_PATTERN, s))

    @classmethod
    def filter_alphabetic_strings(cls, strings):
        return [s for s in strings if cls.is_alphabetic(s)]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test", "!@#"]
    result = StringFilter.filter_alphabetic_strings(sample_values)
    print(result)
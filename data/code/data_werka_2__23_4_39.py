class StringComparator:
    @staticmethod
    def lexical_compare(str1, str2):
        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0

    @staticmethod
    def length_difference(str1, str2):
        return len(str1) - len(str2)

    @classmethod
    def compare_strings(cls, str1, str2):
        lexical_result = cls.lexical_compare(str1, str2)
        length_diff = cls.length_difference(str1, str2)
        return (lexical_result, length_diff)

if __name__ == '__main__':
    sample_str1 = 'apple'
    sample_str2 = 'banana'
    result = StringComparator.compare_strings(sample_str1, sample_str2)
    print(result)
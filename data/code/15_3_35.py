class StringComparator:
    @staticmethod
    def are_strings_equal(str1, str2):
        return str1.lower() == str2.lower()

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "hello"
    result = StringComparator.are_strings_equal(sample_str1, sample_str2)
    print(result)
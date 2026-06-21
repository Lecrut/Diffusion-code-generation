class StringComparator:
    @staticmethod
    def compare(str1, str2):
        return str1 < str2

if __name__ == '__main__':
    sample_str1 = "apple"
    sample_str2 = "banana"
    result = StringComparator.compare(sample_str1, sample_str2)
    print(result)
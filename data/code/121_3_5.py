class StringComparator:
    @staticmethod
    def compare_lexicographically(str1, str2):
        return (str1 > str2) - (str1 < str2)

if __name__ == '__main__':
    sample_str1 = "banana"
    sample_str2 = "apple"
    comparison_result = StringComparator.compare_lexicographically(sample_str1, sample_str2)
    print(comparison_result)
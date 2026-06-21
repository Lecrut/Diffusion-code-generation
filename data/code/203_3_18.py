class StringComparer:
    def compare(self, str1, str2):
        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparer = StringComparer()
    sample_str1 = "zebra"
    sample_str2 = "apple"
    result1 = comparer.compare(sample_str1, sample_str2)
    result2 = comparer.compare("banana", "apple")
    print(result1)
    print(result2)
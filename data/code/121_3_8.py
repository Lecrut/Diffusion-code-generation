class StringComparator:
    @staticmethod
    def compare_lexicographically(str1, str2):
        if str1 > str2:
            return 1
        elif str1 < str2:
            return -1
        else:
            return 0

if __name__ == '__main__':
    comparator = StringComparator()
    result = comparator.compare_lexicographically("apple", "banana")
    print(result)
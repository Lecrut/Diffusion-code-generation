class StringComparator:
    @staticmethod
    def compare_lexicographically(str1, str2):
        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    string_a = "apple"
    string_b = "banana"
    result = StringComparator.compare_lexicographically(string_a, string_b)
    print(result)
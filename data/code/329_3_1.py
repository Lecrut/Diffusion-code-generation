class StringComparer:
    def check_equality(self, str1, str2):
        return str1 == str2
if __name__ == '__main__':
    comparer = StringComparer()
    print(comparer.check_equality("hello", "hello"))
    print(comparer.check_equality("world", "hello"))
    print(comparer.check_equality("", ""))
    print(comparer.check_equality("abc", "abc "))
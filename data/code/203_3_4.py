class StringComparer:
    def compare(self, str1, str2):
        return str1 < str2

if __name__ == '__main__':
    comparer = StringComparer()
    result = comparer.compare("apple", "banana")
    print(result)
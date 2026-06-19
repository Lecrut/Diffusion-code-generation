class StringMerger:
    SEPARATOR = ""

    def merge(self, str1, str2):
        return ''.join([str1, self.SEPARATOR, str2])

if __name__ == '__main__':
    merger = StringMerger()
    string_a = "Hello"
    string_b = "World"
    result = merger.merge(string_a, string_b)
    print(result)
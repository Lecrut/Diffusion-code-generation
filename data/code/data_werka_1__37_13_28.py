class StringMerger:
    SEPARATOR = " and "

    @staticmethod
    def merge(str1, str2):
        return str1 + StringMerger.SEPARATOR + str2

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    merged_string = StringMerger.merge(string_a, string_b)
    print(merged_string)
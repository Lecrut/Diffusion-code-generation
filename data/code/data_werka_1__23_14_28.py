class StringComparator:
    def compare(self, str1, str2):
        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparator = StringComparator()
    string_a = "orange"
    string_b = "grape"
    comparison_result = comparator.compare(string_a, string_b)
    print(comparison_result)
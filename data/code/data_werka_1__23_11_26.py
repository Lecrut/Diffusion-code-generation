class StringComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        diff_length = abs(len(self.str1) - len(self.str2))
        first_diff_index = None

        min_length = min(len(self.str1), len(self.str2))
        for i in range(min_length):
            if self.str1[i] != self.str2[i]:
                first_diff_index = i
                break

        return {
            'length_difference': diff_length,
            'first_different_character_index': first_diff_index
        }

if __name__ == '__main__':
    comparator = StringComparator("apple", "apples")
    result = comparator.compare()
    print(result)
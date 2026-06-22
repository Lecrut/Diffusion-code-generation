class StringComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        len_diff = abs(len(self.str1) - len(self.str2))
        
        min_len = min(len(self.str1), len(self.str2))
        first_diff_index = None
        
        for i in range(min_len):
            if self.str1[i] != self.str2[i]:
                first_diff_index = i
                break

        if first_diff_index is None and len(self.str1) != len(self.str2):
            first_diff_index = min_len

        return {
            'length_difference': len_diff,
            'first_differing_index': first_diff_index
        }

if __name__ == '__main__':
    comparator = StringComparator("apple", "apricot")
    result = comparator.compare()
    print(result)
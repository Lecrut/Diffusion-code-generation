class StringComparator:

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        len_diff = abs(len(self.str1) - len(self.str2))
        min_len = min(len(self.str1), len(self.str2))
        for i in range(min_len):
            if self.str1[i] != self.str2[i]:
                return {'length_difference': len_diff, 'first_differing_index': i}
        return {'length_difference': len_diff, 'first_differing_index': min_len if len(self.str1) != len(self.str2) else None}
if __name__ == '__main__':
    str1 = 'hello'
    str2 = 'helium'
    comparator = StringComparator(str1, str2)
    result = comparator.compare()
    print(result)
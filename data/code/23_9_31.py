class StringComparator:

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        length_diff = len(self.str1) - len(self.str2)
        first_diff_index = None
        min_length = min(len(self.str1), len(self.str2))
        for i in range(min_length):
            if self.str1[i] != self.str2[i]:
                first_diff_index = i
                break
        if first_diff_index is None and length_diff == 0:
            first_diff_index = -1
        return {'length_difference': length_diff, 'first_differing_index': first_diff_index}
if __name__ == '__main__':
    str1 = 'hello'
    str2 = 'helium'
    comparator = StringComparator(str1, str2)
    result = comparator.compare()
    print(result)
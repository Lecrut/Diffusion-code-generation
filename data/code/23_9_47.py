class StringComparator:

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        length_diff = len(self.str1) - len(self.str2)
        index_diff = None
        min_length = min(len(self.str1), len(self.str2))
        for i in range(min_length):
            if self.str1[i] != self.str2[i]:
                index_diff = i
                break
        if index_diff is None and length_diff == 0:
            index_diff = -1
        return {'length_difference': length_diff, 'first_differing_index': index_diff}
if __name__ == '__main__':
    comparator = StringComparator('hello', 'helium')
    result = comparator.compare()
    print(result)
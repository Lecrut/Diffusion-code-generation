class StringComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def calculate_length_difference(self):
        return len(self.str1) - len(self.str2)

    def find_first_differing_index(self):
        min_length = min(len(self.str1), len(self.str2))
        for i in range(min_length):
            if self.str1[i] != self.str2[i]:
                return i
        return -1

    def compare(self):
        length_diff = self.calculate_length_difference()
        first_diff_index = self.find_first_differing_index()
        if first_diff_index is None and length_diff == 0:
            first_diff_index = -1
        return {'length_difference': length_diff, 'first_differing_index': first_diff_index}

if __name__ == '__main__':
    comparator1 = StringComparator('apple', 'apples')
    print(comparator1.compare())

    comparator2 = StringComparator('banana', 'bananas')
    print(comparator2.compare())

    comparator3 = StringComparator('cherry', 'cherrys')
    print(comparator3.compare())
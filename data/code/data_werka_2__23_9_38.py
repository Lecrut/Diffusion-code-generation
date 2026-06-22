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
        return -1 if len(self.str1) == len(self.str2) else None

    def compare(self):
        length_diff = self.calculate_length_difference()
        first_diff_index = self.find_first_differing_index()
        return {'length_difference': length_diff, 'first_differing_index': first_diff_index}

if __name__ == '__main__':
    comparator1 = StringComparator('apple', 'apricot')
    result1 = comparator1.compare()
    print(result1)

    comparator2 = StringComparator('banana', 'bandana')
    result2 = comparator2.compare()
    print(result2)

    comparator3 = StringComparator('cherry', 'cherry')
    result3 = comparator3.compare()
    print(result3)
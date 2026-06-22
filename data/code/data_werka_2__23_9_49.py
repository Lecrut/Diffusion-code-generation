class StringComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def validate_input(self):
        if not isinstance(self.str1, str) or not isinstance(self.str2, str):
            raise ValueError("Both inputs must be strings")

    def calculate_length_difference(self):
        return len(self.str1) - len(self.str2)

    def find_first_differing_index(self):
        min_length = min(len(self.str1), len(self.str2))
        for i in range(min_length):
            if self.str1[i] != self.str2[i]:
                return i
        return -1 if len(self.str1) == len(self.str2) else None

    def compare(self):
        self.validate_input()
        length_diff = self.calculate_length_difference()
        first_diff_index = self.find_first_differing_index()
        return {'length_difference': length_diff, 'first_differing_index': first_diff_index}

if __name__ == '__main__':
    str1 = 'world'
    str2 = 'word'
    comparator = StringComparator(str1, str2)
    result = comparator.compare()
    print(result)
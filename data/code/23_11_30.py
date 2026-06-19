class StringComparison:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.length_diff = abs(len(str1) - len(str2))
        self.first_difference_index = None

    def find_first_difference(self):
        min_length = min(len(self.str1), len(self.str2))
        for i in range(min_length):
            if self.str1[i] != self.str2[i]:
                self.first_difference_index = i
                break
        else:
            if len(self.str1) != len(self.str2):
                self.first_difference_index = min_length

    def __repr__(self):
        return (f"StringComparison("
                f"length_diff={self.length_diff}, "
                f"first_difference_index={self.first_difference_index})")

if __name__ == '__main__':
    str1 = "apple"
    str2 = "apples"
    comparison = StringComparison(str1, str2)
    comparison.find_first_difference()
    print(comparison)
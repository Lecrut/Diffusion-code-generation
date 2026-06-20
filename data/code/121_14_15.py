class StringComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def later_string(self):
        if self.str1 > self.str2:
            return self.str1
        elif self.str2 > self.str1:
            return self.str2
        else:
            return None

if __name__ == '__main__':
    comparator = StringComparator("apple", "banana")
    print(comparator.later_string())
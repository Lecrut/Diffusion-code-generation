class StringComparator:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def later_string(self):
        return max(self.s1, self.s2)

if __name__ == '__main__':
    comparator = StringComparator("apple", "banana")
    print(comparator.later_string())
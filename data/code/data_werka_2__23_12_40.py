class StringComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def compare(self):
        if not isinstance(self.str1, str) or not isinstance(self.str2, str):
            raise ValueError("Both inputs must be strings")
        return (self.str1 > self.str2) - (self.str1 < self.str2)

if __name__ == '__main__':
    comparator = StringComparator("lemon", "lime")
    result1 = comparator.compare()
    print(result1)
    comparator.str1, comparator.str2 = "banana", "apple"
    result2 = comparator.compare()
    print(result2)
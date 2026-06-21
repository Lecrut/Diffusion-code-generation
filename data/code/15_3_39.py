class StringComparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def are_equal(self):
        return self.str1.lower() == self.str2.lower()

if __name__ == '__main__':
    comparator1 = StringComparator("Hello", "hello")
    print(comparator1.are_equal())

    comparator2 = StringComparator("Python", "PYTHON")
    print(comparator2.are_equal())

    comparator3 = StringComparator("World", "world!")
    print(comparator3.are_equal())
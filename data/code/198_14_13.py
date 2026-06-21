class StringMinimizer:
    def __init__(self, strings):
        self.strings = strings

    def find_smallest(self):
        if not self.strings:
            return None
        return min(self.strings)

if __name__ == '__main__':
    minimizer = StringMinimizer(["apple", "banana", "cherry"])
    print(minimizer.find_smallest())
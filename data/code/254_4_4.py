class StringMinimizer:
    def __init__(self, strings):
        self.strings = strings

    def min_by_length(self):
        return min(self.strings, key=len)

if __name__ == '__main__':
    minimizer = StringMinimizer(["apple", "banana", "cherry", "date"])
    print(minimizer.min_by_length())
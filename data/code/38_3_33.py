class StringAnalyzer:
    def __init__(self, s):
        self.s = s

    def has_repeated_letters(self):
        return len(self.s) != len(set(self.s))

if __name__ == '__main__':
    analyzer1 = StringAnalyzer("hello")
    analyzer2 = StringAnalyzer("world")
    analyzer3 = StringAnalyzer("abcde")
    analyzer4 = StringAnalyzer("programming")

    print(f"'{analyzer1.s}': {analyzer1.has_repeated_letters()}")
    print(f"'{analyzer2.s}': {analyzer2.has_repeated_letters()}")
    print(f"'{analyzer3.s}': {analyzer3.has_repeated_letters()}")
    print(f"'{analyzer4.s}': {analyzer4.has_repeated_letters()}")
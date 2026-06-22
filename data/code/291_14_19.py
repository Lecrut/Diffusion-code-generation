class StringLengthComparator:
    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2

    def compare_lengths(self) -> str:
        if len(self.s1) > len(self.s2):
            return f"'{self.s1}' is longer."
        elif len(self.s1) < len(self.s2):
            return f"'{self.s2}' is longer."
        else:
            return "Both strings are equal in length."

if __name__ == '__main__':
    comparator = StringLengthComparator("hello", "world")
    print(comparator.compare_lengths())
    comparator = StringLengthComparator("short", "longerstring")
    print(comparator.compare_lengths())
    comparator = StringLengthComparator("equal", "equal")
    print(comparator.compare_lengths())
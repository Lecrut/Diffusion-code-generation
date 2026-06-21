class StringMerger:
    def __init__(self, part1, part2):
        if not isinstance(part1, str) or not isinstance(part2, str):
            raise ValueError("Both inputs must be strings.")
        self.part1 = part1
        self.part2 = part2

    def merge(self):
        return f"{self.part1}{self.part2}"

if __name__ == '__main__':
    string_first = "Good evening, "
    string_second = "Universe!"
    merger = StringMerger(string_first, string_second)
    result = merger.merge()
    print(result)
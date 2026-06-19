class StringCombiner:
    def __init__(self):
        self.part1 = ""
        self.part2 = ""

    def set_parts(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def combine(self):
        return self.part1 + self.part2

if __name__ == '__main__':
    combiner = StringCombiner()
    combiner.set_parts("Hello, ", "World!")
    combined_result = combiner.combine()
    print(combined_result)
class StringManipulator:
    def __init__(self):
        self.part1 = ""
        self.part2 = ""

    def set_parts(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def combine_strings(self):
        if not self.part1 or not self.part2:
            return ""
        return f"{self.part1} {self.part2}"

if __name__ == '__main__':
    manipulator = StringManipulator()
    manipulator.set_parts("Hello", "World")
    result = manipulator.combine_strings()
    print(result)
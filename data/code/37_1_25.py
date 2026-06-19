class StringManipulator:
    def __init__(self):
        self.part1 = ""
        self.part2 = ""

    def set_parts(self, part1, part2):
        if not isinstance(part1, str) or not isinstance(part2, str):
            raise ValueError("Both parts must be strings")
        self.part1 = part1
        self.part2 = part2

    def combine_strings(self):
        return self.part1 + self.part2

if __name__ == '__main__':
    manipulator = StringManipulator()
    try:
        manipulator.set_parts("Hello", "World")
        result = manipulator.combine_strings()
        print(result)
    except ValueError as e:
        print(e)
class StringManipulator:
    def __init__(self):
        self.part1 = ""
        self.part2 = ""

    def set_part1(self, value):
        if not isinstance(value, str):
            raise ValueError("part1 must be a string")
        self.part1 = value

    def set_part2(self, value):
        if not isinstance(value, str):
            raise ValueError("part2 must be a string")
        self.part2 = value

    def combine_strings(self):
        return self.part1 + self.part2

if __name__ == '__main__':
    manipulator = StringManipulator()
    try:
        manipulator.set_part1("Hello")
        manipulator.set_part2(" World")
        result = manipulator.combine_strings()
        print(result)
    except ValueError as e:
        print(e)
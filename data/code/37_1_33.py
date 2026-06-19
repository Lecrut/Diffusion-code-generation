class StringManipulator:
    def __init__(self):
        self.part1 = "Hello"
        self.part2 = "World"

    def combine_strings(self):
        SEPARATOR = " "
        return self.part1 + SEPARATOR + self.part2

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)
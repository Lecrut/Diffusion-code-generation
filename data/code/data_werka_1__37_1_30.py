class StringManipulator:
    def __init__(self):
        self.part1 = "Good"
        self.part2 = "Morning"

    def combine_strings(self):
        return f"{self.part1} {self.part2}"

if __name__ == '__main__':
    manipulator_instance = StringManipulator()
    combined_result = manipulator_instance.combine_strings()
    print(combined_result)
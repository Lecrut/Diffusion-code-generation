class StringManipulator:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def combine_strings(self):
        return self.string1 + self.string2

if __name__ == '__main__':
    manipulator = StringManipulator("Hello, ", "World!")
    combined_string = manipulator.combine_strings()
    print(combined_string)
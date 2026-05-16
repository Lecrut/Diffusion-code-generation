class StringManipulator:
    def __init__(self):
        self.string1 = ""
        self.string2 = ""
    def combine_strings(self):
        return self.string1 + self.string2
if __name__ == '__main__':
    manipulator = StringManipulator()
    manipulator.string1 = "Hello"
    manipulator.string2 = "World"
    result = manipulator.combine_strings()
    print(result)
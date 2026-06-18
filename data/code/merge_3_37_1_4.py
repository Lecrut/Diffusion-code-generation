class StringManipulator:
    def __init__(self):
        self.string1 = "Hello"
        self.string2 = "World"

    def combine_strings(self):
        """Combines two internal string variables into a single string."""
        return f"{self.string1} {self.string2}"

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)
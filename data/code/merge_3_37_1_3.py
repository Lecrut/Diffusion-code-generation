class StringManipulator:
    def __init__(self):
        self.str1 = "Hello"
        self.str2 = "World"

    def combine_strings(self):
        """Combines two internal string variables into a single string."""
        return f"{self.str1} {self.str2}"

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)
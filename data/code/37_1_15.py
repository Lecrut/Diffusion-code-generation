class StringManipulator:
    def __init__(self):
        self.first_string = "Hello"
        self.second_string = "World"

    def combine_strings(self):
        """Combines two internal string variables into a single string."""
        combined_string = f"{self.first_string} {self.second_string}"
        return combined_string

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)
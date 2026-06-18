class StringManipulator:
    def __init__(self):
        # Internal string variables
        self.string_a = "Hello"
        self.string_b = "World"

    def combine_strings(self):
        """Combines two internal string variables into a single string."""
        combined_string = f"{self.string_a} {self.string_b}"
        return combined_string

if __name__ == '__main__':
    # Create an instance of StringManipulator with hard-coded sample values initialized in the class
    manipulator = StringManipulator()

    # Combine and print the result without any user input or arguments
    result = manipulator.combine_strings()
    print(result)
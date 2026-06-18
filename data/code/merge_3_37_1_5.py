class StringManipulator:
    def __init__(self):
        # Initialize internal string variables with sample data if not provided externally
        self.str_a = "Hello"
        self.str_b = "World"

    def combine_strings(self):
        """Combines two internal string variables into a single string."""
        return f"{self.str_a} {self.str_b}"

if __name__ == '__main__':
    # Create an instance of the StringManipulator class
    manipulator = StringManipulator()

    # Call the method to get the combined result
    result = manipulator.combine_strings()

    # Print the final output (no user input required)
    print(result)
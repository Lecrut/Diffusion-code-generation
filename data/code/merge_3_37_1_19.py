class StringManipulator:
    def __init__(self):
        self.string_a = "Hello"
        self.string_b = ", World!"

    def combine_strings(self) -> str:
        """Combines two internal string variables into a single string."""
        return f"{self.string_a} {self.string_b}"

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)  # Output: Hello, World!
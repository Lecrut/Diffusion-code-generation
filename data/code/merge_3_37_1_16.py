class StringManipulator:
    def __init__(self):
        self.str_a = "Hello"
        self.str_b = "World"

    def combine_strings(self) -> str:
        """Combines two internal string variables into a single string."""
        return f"{self.str_a} {self.str_b}"

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)
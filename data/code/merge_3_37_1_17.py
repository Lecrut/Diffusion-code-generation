class StringManipulator:
    def __init__(self, first_string="", second_string=""):
        self.first_string = first_string
        self.second_string = second_string
    
    def combine_strings(self):
        """Returns a new string formed by concatenating the internal two strings."""
        return f"{self.first_string}{self.second_string}"

if __name__ == '__main__':
    # Hard-coded sample values for testing
    manipulator = StringManipulator("Hello", "World")
    
    result = manipulator.combine_strings()
    
    print(result)
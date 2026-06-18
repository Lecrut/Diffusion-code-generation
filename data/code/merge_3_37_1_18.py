class StringManipulator:
    def __init__(self):
        self.string1 = ""
        self.string2 = ""

    def combine_strings(self):
        """Combines two internal string variables into a single concatenated string."""
        result = f"{self.string1}{self.string2}"
        return result

if __name__ == '__main__':
    manipulator = StringManipulator()
    
    # Hard-coded sample values as per requirements (no user input, args, or files)
    manipulator.string1 = "Hello"
    manipulator.string2 = " World"
    
    combined_result = manipulator.combine_strings()
    
    print(combined_result)
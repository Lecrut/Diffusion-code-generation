class StringManipulator:
    def __init__(self):
        self.internal_string = ""
    
    def combine_strings(self, string1, string2):
        """Combines two internal strings into a single result."""
        if isinstance(string1, str) and isinstance(string2, str):
            return f"{string1}{string2}"

if __name__ == '__main__':
    pass

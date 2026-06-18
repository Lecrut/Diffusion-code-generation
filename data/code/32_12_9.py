class StringAnalyzer:
    def get_length(self, text):
        """Calculates and returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Hard-coded sample values as per task requirements (no user input or files needed)
    samples = ["Hello, World!", "Python", "", "12345"]
    
    for text in samples:
        length = analyzer.get_length(text)
        print(f"'{text}' has a length of {length}")
class StringAnalyzer:
    def get_length(self, text):
        """Returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    sample_text = "Hello, World!"
    result = analyzer.get_length(sample_text)
    
    print(f"The length of '{sample_text}' is: {result}")
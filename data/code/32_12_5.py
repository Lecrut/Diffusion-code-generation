class StringAnalyzer:
    def get_length(self, text):
        """Calculate the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Hard-coded sample values to test without user input or files
    samples = [
        "Hello",
        "",
        "Python Programming is Fun!",
        None  # This will trigger a TypeError in Python as len(None) raises it, demonstrating correct handling logic if extended later.
              # For this specific task focusing on string length, we provide valid strings only.
    ]
    
    print("String Analysis Results:")
    for text in samples:
        result = analyzer.get_length(text)
        print(f"Input '{text}' -> Length: {result}")
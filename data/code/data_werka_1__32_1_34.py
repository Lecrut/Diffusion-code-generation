class StringAnalyzer:
    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_texts = ["Hello World", "Python Programming", "", "a"]
    for text in sample_texts:
        try:
            length = analyzer.get_length(text)
            print(f"Length of '{text}': {length}")
        except ValueError as e:
            print(e)
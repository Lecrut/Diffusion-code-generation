class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    sample_texts = {
        "greeting": "Hello World",
        "programming_language": "Python Programming",
        "empty_string": "",
        "single_char": "a"
    }
    
    analyzer = StringAnalyzer()
    
    for key, value in sample_texts.items():
        print(f"Length of '{key}': {analyzer.get_length(value)}")
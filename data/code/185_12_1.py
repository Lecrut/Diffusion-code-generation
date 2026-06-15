class TextParser:
    def parse(self, text_data):
        import re
        tokens = []
        words = re.findall(r'\b\w+\b', text_data.lower())
        tokens = [word for word in words if word]
        return tokens
if __name__ == '__main__':
    parser = TextParser()
    sample_text = "Hello world! This is a test sentence, isn't it? Python programming is fun."
    cleaned_tokens = parser.parse(sample_text)
    print(cleaned_tokens)
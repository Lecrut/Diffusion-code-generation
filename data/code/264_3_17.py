class TextProcessor:
    def __init__(self, text):
        self.text = text.lower()
        self.tokens = re.findall(r'\b\w+\b', self.text)

    def find_duplicates(self):
        token_count = {}
        duplicates = []
        for token in self.tokens:
            if token_count.get(token) is None:
                token_count[token] = 1
            else:
                token_count[token] += 1
                if token not in duplicates and token_count[token] > 1:
                    duplicates.append(token)
        return duplicates

if __name__ == '__main__':
    sample_text = "This is a large block of text that needs to be processed efficiently. Short words like 'a', 'is', and 'of' should be removed. Performance matters greatly."
    processor = TextProcessor(sample_text)
    result = processor.find_duplicates()
    print(result)
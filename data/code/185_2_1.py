class TextParser:
    def parse_text(self, text):
        tokens = text.lower().split()
        result = {}
        for i in range(len(tokens)):
            if i < len(tokens) - 1:
                key = tokens[i]
                value = tokens[i+1]
            else:
                key = tokens[i]
                value = ""
            result[key] = value
        return result
if __name__ == '__main__':
    parser = TextParser()
    sample_text = "This is a sample sentence for text parsing"
    parsed_data = parser.parse_text(sample_text)
    print(parsed_data)
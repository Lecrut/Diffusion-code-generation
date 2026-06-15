class TextParser:
    def parse_text(self, text):
        tokens = text.lower().split()
        parsed_data = {}
        for i in range(len(tokens)):
            if i % 2 == 0:
                key = tokens[i]
                value = tokens[i+1] if i + 1 < len(tokens) else ""
                parsed_data[key] = value
        return parsed_data
if __name__ == '__main__':
    parser = TextParser()
    sample_text = "apple banana orange grape kiwi"
    result = parser.parse_text(sample_text)
    print(result)
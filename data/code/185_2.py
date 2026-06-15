class TextParser:
    def parse_text(self, text):
        tokens = text.lower().split()
        result = {}
        for i in range(len(tokens)):
            if i % 2 == 0:
                key = tokens[i]
                value = tokens[i+1] if i + 1 < len(tokens) else ""
                result[key] = value
            else:
                pass
        return result
if __name__ == '__main__':
    parser = TextParser()
    sample_text = "apple banana orange grape kiwi"
    parsed_data = parser.parse_text(sample_text)
    print(parsed_data)
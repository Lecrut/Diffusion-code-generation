class NameSeparator:
    def process_text(self, text):
        lines = text.splitlines()
        result = []
        for line in lines:
            names = [name.strip() for name in line.split(',')]
            result.append(names)
        return result
if __name__ == '__main__':
    separator = NameSeparator()
    sample_text = "Alice,Bob\nCharlie,David,Eve\nFrank"
    processed_data = separator.process_text(sample_text)
    print(processed_data)
class NameSeparator:
    def process_text(self, text):
        lines = text.splitlines()
        result = []
        for line in lines:
            names = [name.strip() for name in line.split('\t')]
            if names:
                result.append(names)
        return result

if __name__ == '__main__':
    separator = NameSeparator()
    sample_text = "Alice\tBob\nCharlie\tDavid,Eve\nFrank"
    processed_data = separator.process_text(sample_text)
    print(processed_data)
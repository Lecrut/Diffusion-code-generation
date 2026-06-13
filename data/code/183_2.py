class NameSeparator:
    def process_text(self, text):
        result = {}
        lines = text.split('\n')
        for line in lines:
            if line:
                names = line.split()
                result[line] = names
            else:
                result[line] = []
        return result
if __name__ == '__main__':
    separator = NameSeparator()
    sample_text = "Alice\nBob\nCharlie Brown\nAlice Smith"
    output = separator.process_text(sample_text)
    print(output)
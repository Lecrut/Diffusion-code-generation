class NameSeparator:
    def process_text(self, text):
        lines = text.split('\n')
        result = {}
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
class RunLengthCompressor:
    def __init__(self, text):
        self.text = text
        self.compressed = self.compress()

    def compress(self):
        if not self.text:
            return {}
        counts = {}
        current_char = self.text[0]
        count = 1
        for char in self.text[1:]:
            if char == current_char:
                count += 1
            else:
                counts[current_char] = count
                current_char = char
                count = 1
        counts[current_char] = count
        return counts

    def get_counts(self):
        return self.compressed

if __name__ == '__main__':
    sample_text = "AAABBBCCCDAA"
    compressor = RunLengthCompressor(sample_text)
    result = compressor.get_counts()
    print(result)
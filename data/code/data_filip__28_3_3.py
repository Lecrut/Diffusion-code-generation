class RunLengthCompressor:
    def __init__(self, text):
        self.text = text

    def compress(self):
        if not self.text:
            return {}

        result = {}
        head = self.text[0]
        tally = 1

        for idx in range(1, len(self.text)):
            char = self.text[idx]
            if char == head:
                tally += 1
            else:
                result[head] = tally
                head = char
                tally = 1

        result[head] = tally
        return result

if __name__ == '__main__':
    sample_input = "AAABBBCCD"
    compressor = RunLengthCompressor(sample_input)
    output = compressor.compress()
    print(output)
class RunLengthCompressor:
    def __init__(self):
        self.compressed_result = {}

    def compress(self, text):
        if not text:
            return {}
        counts = {}
        current_char = text[0]
        current_count = 1
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                current_count += 1
            else:
                counts[current_char] = counts.get(current_char, 0) + current_count
                current_char = char
                current_count = 1
        counts[current_char] = counts.get(current_char, 0) + current_count
        self.compressed_result = counts
        return counts

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    sample_input = "aaabbc"
    result = compressor.compress(sample_input)
    print(result)
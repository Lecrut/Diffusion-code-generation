class RunLengthCompressor:
    def __init__(self):
        self.compression_map = {}

    def compress(self, input_string):
        if not input_string:
            return {}
        self.compression_map = {}
        i = 0
        while i < len(input_string):
            char = input_string[i]
            count = 1
            while i + count < len(input_string) and input_string[i + count] == char:
                count += 1
            self.compression_map[char] = count
            i += count
        return self.compression_map

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    sample_input = "AAABBBCCDEEE"
    result = compressor.compress(sample_input)
    print(result)
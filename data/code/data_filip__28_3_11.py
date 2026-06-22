class RunLengthCompressor:
    def __init__(self):
        self.compressed_data = {}

    def compress(self, input_string):
        if not input_string:
            return {}
        self.compressed_data = {}
        count = 1
        for i in range(len(input_string)):
            if i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
                count += 1
            else:
                self.compressed_data[input_string[i]] = count
                count = 1
        return self.compressed_data

if __name__ == '__main__':
    sample_input = "aaabbccccdddaa"
    compressor = RunLengthCompressor()
    result = compressor.compress(sample_input)
    print(result)
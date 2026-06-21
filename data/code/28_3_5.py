class RunLengthCompressor:
    def __init__(self):
        self.compressed_data = {}

    def compress(self, input_string):
        if not input_string:
            return self.compressed_data

        self.compressed_data = {}
        current_char = input_string[0]
        count = 1

        for i in range(1, len(input_string)):
            if input_string[i] == current_char:
                count += 1
            else:
                self.compressed_data[current_char] = count
                current_char = input_string[i]
                count = 1

        self.compressed_data[current_char] = count
        return self.compressed_data

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    result = compressor.compress("aaabbcccaaa")
    print(result)
class RunLengthCompressor:
    def __init__(self):
        self.input_string = ""

    def set_input(self, input_string):
        self.input_string = input_string

    def compress(self):
        if not self.input_string:
            return {}
        counts = {}
        current_char = self.input_string[0]
        current_count = 1
        for i in range(1, len(self.input_string)):
            if self.input_string[i] == current_char:
                current_count += 1
            else:
                counts[current_char] = current_count
                current_char = self.input_string[i]
                current_count = 1
        counts[current_char] = current_count
        return counts

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    compressor.set_input("aaabbc")
    result = compressor.compress()
    print(result)
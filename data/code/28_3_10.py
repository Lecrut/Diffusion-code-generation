class RunLengthCompressor:
    def __init__(self, input_string):
        self.input_string = input_string

    def compress(self):
        if not self.input_string:
            return {}
        result = {}
        current_char = self.input_string[0]
        count = 1
        for char in self.input_string[1:]:
            if char == current_char:
                count += 1
            else:
                result[current_char] = count
                current_char = char
                count = 1
        result[current_char] = count
        return result

if __name__ == '__main__':
    compressor = RunLengthCompressor("AAABBBCCCDAA")
    print(compressor.compress())
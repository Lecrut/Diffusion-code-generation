class RunLengthCompressor:
    def __init__(self, input_string: str):
        self.input_string = input_string

    def compress(self):
        if not self.input_string:
            return {}

        result = {}
        current_char = self.input_string[0]
        count = 1

        for i in range(1, len(self.input_string)):
            char = self.input_string[i]
            if char == current_char:
                count += 1
            else:
                result[current_char] = count
                current_char = char
                count = 1

        result[current_char] = count
        return result

if __name__ == '__main__':
    compressor = RunLengthCompressor("AAABBBCCCA")
    print(compressor.compress())
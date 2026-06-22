class RunLengthCompressor:
    def __init__(self, input_string: str):
        self.input_string = input_string

    def compress(self) -> dict:
        if not self.input_string:
            return {}

        counts = []
        chars = []
        current_char = self.input_string[0]
        count = 1

        for i in range(1, len(self.input_string)):
            char = self.input_string[i]
            if char == current_char:
                count += 1
            else:
                counts.append(count)
                chars.append(current_char)
                current_char = char
                count = 1

        counts.append(count)
        chars.append(current_char)

        result = {}
        for c, cnt in zip(chars, counts):
            result[c] = cnt
        return result

if __name__ == '__main__':
    compressor = RunLengthCompressor("aabbbcccc")
    result = compressor.compress()
    print(result)
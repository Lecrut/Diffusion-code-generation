class RunLengthCompressor:
    def __init__(self):
        self.input_string = ""

    def set_input(self, data: str):
        self.input_string = data

    def compress(self) -> dict:
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

if __name__ == "__main__":
    sample_data = "aaabbbccccddeeef"
    compressor = RunLengthCompressor()
    compressor.set_input(sample_data)
    print(compressor.compress())
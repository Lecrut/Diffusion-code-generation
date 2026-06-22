class RunLengthCompressor:
    def __init__(self):
        self.separator = "#"

    def encode(self, text):
        if not text:
            return ""
        result = []
        current_char = text[0]
        run_length = 1
        for index in range(1, len(text)):
            char = text[index]
            if char == current_char:
                run_length += 1
            else:
                result.append(str(run_length) + current_char)
                current_char = char
                run_length = 1
        result.append(str(run_length) + current_char)
        return "".join(result)

    def decode(self, compressed_text):
        if not compressed_text:
            return ""
        result = []
        index = 0
        while index < len(compressed_text):
            digit_start = index
            while index < len(compressed_text) and compressed_text[index].isdigit():
                index += 1
            if index == digit_start:
                raise ValueError("Invalid format: expected a digit count")
            count = int(compressed_text[digit_start:index])
            if index >= len(compressed_text):
                raise ValueError("Invalid format: missing character after count")
            char = compressed_text[index]
            index += 1
            result.append(char * count)
        return "".join(result)

if __name__ == "__main__":
    compressor = RunLengthCompressor()
    original_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_version = compressor.encode(original_string)
    decoded_version = compressor.decode(encoded_version)
    print(encoded_version)
    print(decoded_version)
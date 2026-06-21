class RLECompressor:
    def __init__(self, separator=""):
        self.separator = separator

    def encode(self, data: str) -> str:
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        
        result.append(f"{count}{current_char}")
        return self.separator.join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressor = RLECompressor()
    encoded_output = compressor.encode(sample_input)
    print(encoded_output)
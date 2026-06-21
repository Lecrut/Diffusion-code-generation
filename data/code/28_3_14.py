class RunLengthCompressor:
    def __init__(self):
        self.output_dict = {}

    def compress(self, text):
        if not text:
            return {}
        
        result = {}
        current_char = text[0]
        count = 1
        
        index = 1
        length = len(text)
        
        while index < length:
            char = text[index]
            if char == current_char:
                count += 1
            else:
                result[current_char] = count
                current_char = char
                count = 1
            index += 1
        
        result[current_char] = count
        return result

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    sample_text = "AAAABBBCCDAA"
    output = compressor.compress(sample_text)
    print(output)
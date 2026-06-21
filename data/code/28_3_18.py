class RunLengthCompressor:
    def __init__(self):
        self.input_string = ""

    def set_input(self, text):
        self.input_string = text

    def compress(self, text):
        if not text:
            return {}
        compressed_dict = {}
        i = 0
        while i < len(text):
            current_char = text[i]
            count = 1
            while i + 1 < len(text) and text[i + 1] == current_char:
                count += 1
                i += 1
            if current_char in compressed_dict:
                compressed_dict[current_char] += count
            else:
                compressed_dict[current_char] = count
            i += 1
        return compressed_dict

    def process_hardcoded_input(self):
        test_data = "AABBBCCCCDDDEEEFFFFFG"
        self.set_input(test_data)
        return self.compress(self.input_string)

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    result = compressor.process_hardcoded_input()
    print(result)
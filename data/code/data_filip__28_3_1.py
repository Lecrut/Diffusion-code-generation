class RunLengthCompressor:
    def __init__(self):
        self.input_string = ""

    def set_input(self, data):
        self.input_string = data

    def compress(self):
        if not self.input_string:
            return {}
        
        result = {}
        count = 1
        current_char = self.input_string[0]

        for i in range(1, len(self.input_string)):
            if self.input_string[i] == current_char:
                count += 1
            else:
                result[current_char] = count
                current_char = self.input_string[i]
                count = 1
        
        result[current_char] = count
        return result

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    compressor.set_input("AAABBCDDDEEE")
    print(compressor.compress())
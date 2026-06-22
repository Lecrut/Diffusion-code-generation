class RunLengthCompressor:
    def __init__(self, text):
        self.text = text

    def compress(self):
        if not self.text:
            return {}
        
        result = {}
        if self.text[0] == ' ':
            result[' '] = 1
            remaining = self.text[1:]
        else:
            current_char = self.text[0]
            count = 1
            i = 1
            while i < len(self.text):
                char = self.text[i]
                if char == current_char:
                    count += 1
                else:
                    result[current_char] = count
                    current_char = char
                    count = 1
                i += 1
            result[current_char] = count
        
        return result

if __name__ == '__main__':
    compressor = RunLengthCompressor("aaabbc")
    print(compressor.compress())
class RunLengthCompressor:
    def __init__(self, input_string):
        self.input_string = input_string

    def process(self):
        if not self.input_string:
            return {}
        result = {}
        count = 0
        current_char = self.input_string[0]
        for char in self.input_string:
            if char == current_char:
                count += 1
            else:
                if current_char in result:
                    result[current_char] += count
                else:
                    result[current_char] = count
                current_char = char
                count = 1
        if current_char in result:
            result[current_char] += count
        else:
            result[current_char] = count
        return result

if __name__ == '__main__':
    compressor = RunLengthCompressor("AAABBC")
    output = compressor.process()
    print(output)
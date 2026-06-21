class RunLengthEncoder:
    def __init__(self):
        self.buffer = []

    def encode(self, data):
        if not data:
            return ""
        self.buffer.clear()
        length = len(data)
        idx = 0
        while idx < length:
            char = data[idx]
            run_length = 1
            idx += 1
            while idx < length and data[idx] == char:
                run_length += 1
                idx += 1
            self.buffer.append(str(run_length))
            self.buffer.append(char)
        return "".join(self.buffer)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "aaabbbccccdddeeefffggg"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    
    sample_input_two = "x"
    encoded_result_two = encoder.encode(sample_input_two)
    print(encoded_result_two)
    
    sample_input_three = ""
    encoded_result_three = encoder.encode(sample_input_three)
    print(encoded_result_three)
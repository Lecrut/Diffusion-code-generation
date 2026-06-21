class RunLengthEncoder:
    def __init__(self, input_string):
        self.input_string = input_string

    def encode(self):
        if not self.input_string:
            return []
        result = []
        current_char = self.input_string[0]
        count = 1
        for char in self.input_string[1:]:
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder("aabbbc")
    print(encoder.encode())
    encoder_empty = RunLengthEncoder("")
    print(encoder_empty.encode())
    encoder_single = RunLengthEncoder("z")
    print(encoder_single.encode())
    encoder_complex = RunLengthEncoder("aaabbaaccc")
    print(encoder_complex.encode())
class RunLengthEncoder:
    def __init__(self, input_string):
        self.input_string = input_string

    def encode(self):
        if not self.input_string:
            return ""

        encoded = []
        current_char = self.input_string[0]
        count = 1

        for i in range(1, len(self.input_string)):
            if self.input_string[i] == current_char:
                count += 1
            else:
                encoded.append(str(count) + current_char)
                current_char = self.input_string[i]
                count = 1

        encoded.append(str(count) + current_char)
        return "".join(encoded)

if __name__ == "__main__":
    sample_string = "AAABBBCCDAA"
    encoder = RunLengthEncoder(sample_string)
    result = encoder.encode()
    print(result)
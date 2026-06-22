class RunLengthEncoder:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string

    def encode(self) -> list:
        encoded = []
        if not self.input_string:
            return encoded

        current_char = self.input_string[0]
        count = 1

        for i in range(1, len(self.input_string)):
            char = self.input_string[i]
            if char == current_char:
                count += 1
            else:
                encoded.append((current_char, count))
                current_char = char
                count = 1
        encoded.append((current_char, count))
        return encoded

if __name__ == '__main__':
    encoder = RunLengthEncoder("AAABBBCCDAA")
    result = encoder.encode()
    print(result)
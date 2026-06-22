class RunLengthEncoder:
    def __init__(self):
        self.last_encoded = None

    def encode(self, data):
        if not data:
            self.last_encoded = ""
            return self.last_encoded
        encoded_parts = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                encoded_parts.append(str(count) + current_char)
                current_char = data[i]
                count = 1
        encoded_parts.append(str(count) + current_char)
        self.last_encoded = "".join(encoded_parts)
        return self.last_encoded

    def get_result(self):
        return self.last_encoded

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoder = RunLengthEncoder()
    result = encoder.encode(sample_input)
    print(result)
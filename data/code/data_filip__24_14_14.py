class RunLengthEncoder:
    def __init__(self, data):
        self.data = data

    def encode(self):
        if not self.data:
            return []
        result = []
        count = 1
        current_char = self.data[0]
        for char in self.data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        result.append((current_char, count))
        return result

    def decode(self, encoded_data):
        result = []
        for char, count in encoded_data:
            result.extend([char] * count)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder("AAABBBCCC")
    encoded = encoder.encode()
    print(encoded)
    print(encoder.decode(encoded))
class RunLengthEncoder:
    def __init__(self, data):
        self.data = data

    def encode(self):
        if not self.data:
            return []
        result = []
        current_char = self.data[0]
        count = 1
        for i in range(1, len(self.data)):
            if self.data[i] == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = self.data[i]
                count = 1
        result.append((current_char, count))
        return result

    def decode(self, encoded_data):
        result = []
        for char, count in encoded_data:
            result.append(char * count)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder("AAABBBCCDAA")
    encoded = encoder.encode()
    print(encoded)
    decoded = encoder.decode(encoded)
    print(decoded)
class RLEHandler:
    def __init__(self, data):
        self.data = data

    def encode(self):
        if not self.data:
            return []
        encoded = []
        current_char = self.data[0]
        count = 1
        for i in range(1, len(self.data)):
            if self.data[i] == current_char:
                count += 1
            else:
                encoded.append((current_char, count))
                current_char = self.data[i]
                count = 1
        encoded.append((current_char, count))
        return encoded

    def decode(self, encoded_data):
        decoded = []
        for char, count in encoded_data:
            decoded.extend([char] * count)
        return decoded

if __name__ == '__main__':
    sample_data = "aaabbbcccaabb"
    handler = RLEHandler(sample_data)
    encoded_result = handler.encode()
    print(encoded_result)
    decoded_result = handler.decode(encoded_result)
    print(decoded_result)
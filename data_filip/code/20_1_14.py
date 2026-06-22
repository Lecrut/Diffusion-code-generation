class RLEEncoder:
    def __init__(self, data):
        self.data = data

    def encode(self):
        if not self.data:
            return []
        result = []
        current = self.data[0]
        count = 1
        for val in self.data[1:]:
            if val == current:
                count += 1
            else:
                result.append([current, count])
                current = val
                count = 1
        result.append([current, count])
        return result

    def decode(self):
        if not self.data:
            return []
        decoded = []
        for pair in self.data:
            value, times = pair
            decoded.extend([value] * times)
        return decoded

if __name__ == '__main__':
    sample_list = [5, 5, 5, 8, 8, 2, 2, 2, 2, 2, 9, 7, 7, 7]
    encoder = RLEEncoder(sample_list)
    encoded_result = encoder.encode()
    print(encoded_result)
    encoder.data = encoded_result
    decoded_result = encoder.decode()
    print(decoded_result)
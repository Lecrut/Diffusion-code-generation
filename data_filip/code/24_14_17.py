class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return []
        encoded = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                encoded.append((current_char, count))
                current_char = data[i]
                count = 1
        encoded.append((current_char, count))
        return encoded

    def decode(self, encoded_data):
        if not encoded_data:
            return ""
        decoded = []
        for char, count in encoded_data:
            decoded.append(char * count)
        return "".join(decoded)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_string)
    print(encoded_result)
    decoded_result = encoder.decode(encoded_result)
    print(decoded_result)
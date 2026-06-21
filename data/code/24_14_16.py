class RunLengthEncoder:
    @staticmethod
    def encode(data):
        if not data:
            return []
        encoded = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded.append((data[i - 1], count))
                count = 1
        encoded.append((data[-1], count))
        return encoded

    @staticmethod
    def decode(encoded_data):
        decoded = []
        for char, count in encoded_data:
            decoded.append(char * count)
        return "".join(decoded)

if __name__ == "__main__":
    sample_input = "aaabbccccd"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_input)
    decoded_result = encoder.decode(encoded_result)
    print(encoded_result)
    print(decoded_result)
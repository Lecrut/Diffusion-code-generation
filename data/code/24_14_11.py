class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return ""
        encoded = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(f"{current_char}{count}")
                current_char = char
                count = 1
        encoded.append(f"{current_char}{count}")
        return "".join(encoded)

    def decode(self, data):
        if not data:
            return ""
        decoded = []
        i = 0
        while i < len(data):
            if i + 1 < len(data) and data[i+1].isdigit():
                char = data[i]
                count = int(data[i+1])
                decoded.append(char * count)
                i += 2
            else:
                decoded.append(data[i])
                i += 1
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "aaabbccccd"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    decoded_result = encoder.decode(encoded_result)
    print(decoded_result)
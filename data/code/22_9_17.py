class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        encoded = []
        count = 1
        current_char = s[0]
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                encoded.append(f"{count}{current_char}")
                current_char = s[i]
                count = 1
        encoded.append(f"{count}{current_char}")
        return "".join(encoded)

    def decode(self, encoded):
        if not encoded:
            return ""
        decoded = []
        i = 0
        while i < len(encoded):
            count = 0
            while i < len(encoded) and encoded[i].isdigit():
                count = count * 10 + int(encoded[i])
                i += 1
            if i < len(encoded):
                char = encoded[i]
                decoded.append(char * count)
                i += 1
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "AAABBBCCD"
    encoded = encoder.encode(sample_input)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)
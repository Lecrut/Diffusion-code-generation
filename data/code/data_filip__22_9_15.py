class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        encoded = []
        current_char = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                encoded.append(f"{count}{current_char}")
                current_char = s[i]
                count = 1
        encoded.append(f"{count}{current_char}")
        return "".join(encoded)

    def decode(self, s):
        if not s:
            return ""
        decoded = []
        i = 0
        while i < len(s):
            count_str = ""
            while i < len(s) and s[i].isdigit():
                count_str += s[i]
                i += 1
            if count_str:
                count = int(count_str)
            else:
                count = 1
            if i < len(s):
                char = s[i]
                i += 1
                decoded.append(char * count)
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "AAABBBCCDAA"
    encoded = encoder.encode(sample_string)
    decoded = encoder.decode(encoded)
    print(f"Original: {sample_string}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    sample_string2 = "abcdef"
    encoded2 = encoder.encode(sample_string2)
    decoded2 = encoder.decode(encoded2)
    print(f"Original: {sample_string2}")
    print(f"Encoded: {encoded2}")
    print(f"Decoded: {decoded2}")
    sample_string3 = ""
    encoded3 = encoder.encode(sample_string3)
    decoded3 = encoder.decode(encoded3)
    print(f"Original: '{sample_string3}'")
    print(f"Encoded: '{encoded3}'")
    print(f"Decoded: '{decoded3}'")
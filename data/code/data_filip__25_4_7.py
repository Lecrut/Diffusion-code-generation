class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        result = []
        current_char = s[0]
        count = 1
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decode(self, encoded):
        if not encoded:
            return ""
        result = []
        count = ""
        for char in encoded:
            if char.isdigit():
                count += char
            else:
                result.append(char * int(count))
                count = ""
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "AAAABBBCCDAA"
    encoded = encoder.encode(original)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)
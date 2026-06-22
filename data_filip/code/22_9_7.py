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
                encoded.append(str(count) + current_char)
                current_char = s[i]
                count = 1
        encoded.append(str(count) + current_char)
        return "".join(encoded)

    def decode(self, s):
        if not s:
            return ""
        decoded = []
        i = 0
        while i < len(s):
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            if i < len(s):
                char = s[i]
                decoded.append(char * int(num))
                i += 1
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "aaabbbcccaaabbbccc"
    encoded = encoder.encode(original)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)
class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        encoded = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                encoded.append(s[i - 1] + str(count))
                count = 1
        encoded.append(s[-1] + str(count))
        return "".join(encoded)

    def decode(self, encoded):
        decoded = []
        i = 0
        while i < len(encoded):
            char = encoded[i]
            j = i + 1
            while j < len(encoded) and encoded[j].isdigit():
                j += 1
            count = int(encoded[i + 1:j]) if i + 1 < j else 1
            decoded.append(char * count)
            i = j
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "AAABBBCCD"
    encoded = encoder.encode(original)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)
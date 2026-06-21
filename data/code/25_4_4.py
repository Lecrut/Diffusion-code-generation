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
                encoded.append(str(count) + s[i - 1])
                count = 1
        encoded.append(str(count) + s[-1])
        return "".join(encoded)

    def decode(self, s):
        if not s:
            return ""
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            if j == i:
                break
            count = int(s[i:j])
            char = s[j]
            decoded.append(char * count)
            i = j + 1
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_string = "AAAABBBCCDA"
    encoded_result = encoder.encode(test_string)
    decoded_result = encoder.decode(encoded_result)
    print(encoded_result)
    print(decoded_result)
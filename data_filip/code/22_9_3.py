class RLEEncoder:
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
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            char = s[j]
            decoded.append(char * count)
            i = j + 1
        return "".join(decoded)

if __name__ == '__main__':
    rle = RLEEncoder()
    test_string = "aaabbbcccc"
    encoded_result = rle.encode(test_string)
    decoded_result = rle.decode(encoded_result)
    print(encoded_result)
    print(decoded_result)
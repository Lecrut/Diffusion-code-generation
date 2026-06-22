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
                encoded.append(str(count) + current_char)
                current_char = s[i]
                count = 1
        encoded.append(str(count) + current_char)
        return "".join(encoded)

    def decode(self, encoded_str):
        if not encoded_str:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_str):
            count_str = ""
            while i < len(encoded_str) and encoded_str[i].isdigit():
                count_str += encoded_str[i]
                i += 1
            if count_str:
                count = int(count_str)
                char = encoded_str[i]
                decoded.append(char * count)
                i += 1
            else:
                break
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "AAABBBCCD"
    encoded = encoder.encode(sample_string)
    print(encoded)
    decoded = encoder.decode(encoded)
    print(decoded)
class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        result = []
        count = 1
        current_char = s[0]
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(str(count))
                result.append(current_char)
                current_char = char
                count = 1
        result.append(str(count))
        result.append(current_char)
        return "".join(result)

    def decode(self, encoded_s):
        if not encoded_s:
            return ""
        result = []
        i = 0
        while i < len(encoded_s):
            count_str = ""
            while i < len(encoded_s) and encoded_s[i].isdigit():
                count_str += encoded_s[i]
                i += 1
            if i < len(encoded_s):
                count = int(count_str)
                char = encoded_s[i]
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "AAABBBCCCCDDDEE"
    encoded = encoder.encode(original)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)
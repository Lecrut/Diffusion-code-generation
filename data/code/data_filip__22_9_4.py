class RunLengthEncoder:
    def encode(self, string):
        if not string:
            return ""
        encoded = []
        current_char = string[0]
        count = 1
        for char in string[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(str(count) + current_char)
                current_char = char
                count = 1
        encoded.append(str(count) + current_char)
        return "".join(encoded)

    def decode(self, encoded_string):
        if not encoded_string:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_string):
            count = ""
            while i < len(encoded_string) and encoded_string[i].isdigit():
                count += encoded_string[i]
                i += 1
            char = encoded_string[i]
            i += 1
            decoded.append(char * int(count))
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "aaabbc"
    encoded = encoder.encode(sample_string)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)
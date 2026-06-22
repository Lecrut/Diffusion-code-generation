class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        result = []
        count = 1
        current_char = text[0]
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = text[i]
                count = 1
        result.append(str(count) + current_char)
        return "".join(result)

    def decode(self, encoded_text):
        if not encoded_text:
            return ""
        result = []
        i = 0
        while i < len(encoded_text):
            digit_str = ""
            while i < len(encoded_text) and encoded_text[i].isdigit():
                digit_str += encoded_text[i]
                i += 1
            count = int(digit_str)
            if i < len(encoded_text):
                char = encoded_text[i]
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    rle = RunLengthEncoder()
    original = "AAABBBCCCCDDD"
    encoded = rle.encode(original)
    decoded = rle.decode(encoded)
    print(encoded)
    print(decoded)
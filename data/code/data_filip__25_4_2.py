class RLE:
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
                result.append(f"{count}{current_char}")
                current_char = text[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decode(self, encoded_text):
        if not encoded_text:
            return ""
        result = []
        i = 0
        while i < len(encoded_text):
            count_str = ""
            while i < len(encoded_text) and encoded_text[i].isdigit():
                count_str += encoded_text[i]
                i += 1
            if i < len(encoded_text):
                char = encoded_text[i]
                result.append(char * int(count_str))
                i += 1
        return "".join(result)

if __name__ == '__main__':
    rle = RLE()
    original = "aaaabbbcc"
    encoded = rle.encode(original)
    print(encoded)
    decoded = rle.decode(encoded)
    print(decoded)
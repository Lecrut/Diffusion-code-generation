class RLE:
    def encode(self, text):
        if not text:
            return ""
        encoded = []
        current_char = text[0]
        count = 1
        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(f"{count}{current_char}")
                current_char = char
                count = 1
        encoded.append(f"{count}{current_char}")
        return "".join(encoded)

    def decode(self, text):
        if not text:
            return ""
        decoded = []
        i = 0
        while i < len(text):
            count_str = ""
            while i < len(text) and text[i].isdigit():
                count_str += text[i]
                i += 1
            if i < len(text):
                char = text[i]
                count = int(count_str)
                decoded.append(char * count)
                i += 1
        return "".join(decoded)

if __name__ == '__main__':
    rle = RLE()
    original = "AAABBC"
    encoded = rle.encode(original)
    decoded = rle.decode(encoded)
    print(encoded)
    print(decoded)
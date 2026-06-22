class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        result = []
        current_char = text[0]
        count = 1
        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = char
                count = 1
        result.append(str(count) + current_char)
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    print(encoder.encode("AABBBCC"))
    print(encoder.encode("ABC"))
    print(encoder.encode(""))
    print(encoder.encode("A"))
    print(encoder.encode("AAAAAAAAAA"))
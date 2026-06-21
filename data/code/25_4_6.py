class RunLength:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        encoded_parts = []
        current_char = text[0]
        count = 1
        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                encoded_parts.append(f"{count}{current_char}")
                current_char = char
                count = 1
        encoded_parts.append(f"{count}{current_char}")
        return "".join(encoded_parts)

    def decode(self, text: str) -> str:
        if not text:
            return ""
        decoded_parts = []
        i = 0
        while i < len(text):
            if text[i].isdigit():
                num_start = i
                while i < len(text) and text[i].isdigit():
                    i += 1
                count = int(text[num_start:i])
                if i < len(text):
                    char = text[i]
                    decoded_parts.append(char * count)
                    i += 1
            else:
                decoded_parts.append(text[i])
                i += 1
        return "".join(decoded_parts)

if __name__ == '__main__':
    encoder = RunLength()
    original_text = "AAABBBCCC"
    encoded_text = encoder.encode(original_text)
    print(encoded_text)
    decoded_text = encoder.decode(encoded_text)
    print(decoded_text)
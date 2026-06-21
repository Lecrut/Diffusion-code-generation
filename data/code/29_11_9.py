class RunLengthEncoder:
    def __init__(self):
        self.name = "RunLengthEncoder"

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
                encoded.append(f"{current_char}{count}")
                current_char = char
                count = 1
        encoded.append(f"{current_char}{count}")
        return "".join(encoded)

    def decode(self, encoded_text):
        if not encoded_text:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_text):
            char = encoded_text[i]
            i += 1
            num_str = []
            while i < len(encoded_text) and encoded_text[i].isdigit():
                num_str.append(encoded_text[i])
                i += 1
            count = int("".join(num_str)) if num_str else 1
            decoded.append(char * count)
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    samples = [
        "AABBBCCCC",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWWWWWWWWWWW",
        "ABC",
        "A",
        "",
        "AAABBBCCC"
    ]
    for sample in samples:
        encoded = encoder.encode(sample)
        decoded = encoder.decode(encoded)
        print(f"Original: '{sample}'")
        print(f"Encoded:  '{encoded}'")
        print(f"Decoded:  '{decoded}'")
        print(f"Match:    {sample == decoded}")
        print()
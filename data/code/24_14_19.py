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
                encoded.append(f"{count}{current_char}")
                current_char = char
                count = 1

        encoded.append(f"{count}{current_char}")
        return "".join(encoded)

    def decode(self, encoded_string):
        if not encoded_string:
            return ""

        decoded = []
        i = 0
        while i < len(encoded_string):
            count = 0
            while i < len(encoded_string) and encoded_string[i].isdigit():
                count = count * 10 + int(encoded_string[i])
                i += 1

            if i < len(encoded_string):
                char = encoded_string[i]
                decoded.append(char * count)
                i += 1

        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()

    sample_strings = [
        "AAAABBBCCDAA",
        "A",
        "ABABAB",
        "",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    ]

    for s in sample_strings:
        encoded = encoder.encode(s)
        decoded = encoder.decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded!r}")
        print(f"Match:    {s == decoded}")
        print()
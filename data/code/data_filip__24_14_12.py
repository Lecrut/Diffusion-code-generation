class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return ""

        encoded = []
        current_char = data[0]
        count = 1

        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(str(count) + current_char)
                current_char = char
                count = 1

        encoded.append(str(count) + current_char)
        return "".join(encoded)

    def decode(self, encoded_data):
        if not encoded_data:
            return ""

        decoded = []
        i = 0
        while i < len(encoded_data):
            count_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                count_str += encoded_data[i]
                i += 1
            if count_str:
                count = int(count_str)
                if i < len(encoded_data):
                    char = encoded_data[i]
                    i += 1
                    decoded.append(char * count)
            else:
                if i < len(encoded_data):
                    decoded.append(encoded_data[i])
                    i += 1

        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()

    sample_strings = [
        "AAAABBBCCDAA",
        "ABCDE",
        "A",
        "",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWWWWWWWWWWW"
    ]

    for s in sample_strings:
        encoded = encoder.encode(s)
        decoded = encoder.decode(encoded)
        print(f"Original:  {s}")
        print(f"Encoded:   {encoded}")
        print(f"Decoded:   {decoded}")
        print(f"Match:     {s == decoded}")
        print()
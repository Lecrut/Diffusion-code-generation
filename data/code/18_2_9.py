class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        result = []
        current_char = s[0]
        count = 1
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "AAABBBCCDAA"
    encoded = encoder.encode(sample_string)
    print(encoded)
    empty_string = ""
    print(encoder.encode(empty_string))
    single_char = "Z"
    print(encoder.encode(single_char))
    complex_string = "aabbbcdddddeefffff"
    print(encoder.encode(complex_string))
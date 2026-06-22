import re

class RunLengthEncoder:
    def __init__(self):
        self.pattern = re.compile(r'(.)\1*')

    def encode(self, text: str) -> str:
        if not text:
            return ""
        matches = self.pattern.finditer(text)
        parts = []
        for match in matches:
            char = match.group(1)
            count = match.end() - match.start()
            if count > 1:
                parts.append(f"{count}{char}")
            else:
                parts.append(char)
        return "".join(parts)

    def decode(self, text: str) -> str:
        if not text:
            return ""
        pattern = re.compile(r'(\d*)(.)')
        matches = pattern.finditer(text)
        parts = []
        for match in matches:
            count_str = match.group(1)
            char = match.group(2)
            if count_str:
                count = int(count_str)
                parts.append(char * count)
            else:
                parts.append(char)
        return "".join(parts)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_text = "aabbbccccddddeeeee"
    encoded_result = encoder.encode(sample_text)
    print(encoded_result)
    decoded_result = encoder.decode(encoded_result)
    print(decoded_result)
    complex_text = "abcde"
    encoded_complex = encoder.encode(complex_text)
    print(encoded_complex)
    decoded_complex = encoder.decode(encoded_complex)
    print(decoded_complex)
    long_sequence = "a" * 15 + "b" * 2 + "c"
    encoded_long = encoder.encode(long_sequence)
    print(encoded_long)
    decoded_long = encoder.decode(encoded_long)
    print(decoded_long)
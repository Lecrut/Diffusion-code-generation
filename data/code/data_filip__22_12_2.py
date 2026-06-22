class RLEHandler:
    def compress(self, text: str) -> str:
        if not text:
            return ""
        compressed = []
        count = 1
        length = len(text)
        for i in range(length):
            char = text[i]
            if i + 1 < length and text[i + 1] == char:
                count += 1
            else:
                if count > 1:
                    compressed.append(f"{count}{char}")
                else:
                    compressed.append(char)
                count = 1
        return "".join(compressed)

    def decompress(self, text: str) -> str:
        if not text:
            return ""
        decompressed = []
        length = len(text)
        i = 0
        while i < length:
            char = text[i]
            if char.isdigit():
                count_str = char
                i += 1
                while i < length and text[i].isdigit():
                    count_str += text[i]
                    i += 1
                count = int(count_str)
                if i < length:
                    next_char = text[i]
                    decompressed.append(next_char * count)
                    i += 1
            else:
                decompressed.append(char)
                i += 1
        return "".join(decompressed)

if __name__ == '__main__':
    handler = RLEHandler()
    original = "aaabbccccdaa"
    compressed = handler.compress(original)
    decompressed = handler.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Round-trip valid: {original == decompressed}")
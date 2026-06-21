class RunLengthEncoding:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        compressed = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = char
                count = 1
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    @staticmethod
    def decompress(data: str) -> str:
        if not data:
            return ""
        decompressed = []
        i = 0
        while i < len(data):
            num_str = []
            while i < len(data) and data[i].isdigit():
                num_str.append(data[i])
                i += 1
            count = int("".join(num_str))
            if i < len(data):
                char = data[i]
                i += 1
                decompressed.append(char * count)
        return "".join(decompressed)

if __name__ == '__main__':
    test_data = "aaabbbccc"
    encoded = RunLengthEncoding.compress(test_data)
    decoded = RunLengthEncoding.decompress(encoded)
    print(f"Original: {test_data}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {test_data == decoded}")
    
    empty_data = ""
    empty_encoded = RunLengthEncoding.compress(empty_data)
    empty_decoded = RunLengthEncoding.decompress(empty_encoded)
    print(f"Empty Original: '{empty_data}'")
    print(f"Empty Encoded: '{empty_encoded}'")
    print(f"Empty Decoded: '{empty_decoded}'")
    
    single_char_data = "aaaaa"
    single_encoded = RunLengthEncoding.compress(single_char_data)
    single_decoded = RunLengthEncoding.decompress(single_encoded)
    print(f"Single Char Original: '{single_char_data}'")
    print(f"Single Char Encoded: '{single_encoded}'")
    print(f"Single Char Decoded: '{single_decoded}'")
    print(f"Single Char Match: {single_char_data == single_decoded}")
    
    mixed_data = "a2b3c"
    mixed_decoded = RunLengthEncoding.decompress(mixed_data)
    print(f"Mixed Decoded: '{mixed_decoded}'")
    print(f"Mixed Expected: 'aaabbccc'")
    print(f"Mixed Match: {mixed_decoded == 'aaabbccc'}")
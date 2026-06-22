class RunLengthEncoder:
    @staticmethod
    def compress(text: str) -> str:
        if not text:
            return ""
        
        compressed = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = text[i]
                count = 1
        
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    @staticmethod
    def decompress(encoded_text: str) -> str:
        if not encoded_text:
            return ""
        
        decompressed = []
        i = 0
        n = len(encoded_text)
        
        while i < n:
            count_str = ""
            while i < n and encoded_text[i].isdigit():
                count_str += encoded_text[i]
                i += 1
            
            if i < n:
                count = int(count_str)
                char = encoded_text[i]
                decompressed.append(char * count)
                i += 1
        
        return "".join(decompressed)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "AAAABBBCCDAA"
    compressed = encoder.compress(original)
    print(compressed)
    decompressed = encoder.decompress(compressed)
    print(decompressed)
    print(compressed == "4A3B2C1D2A")
    print(decompressed == original)
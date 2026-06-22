class RLECompressor:
    def compress(self, text):
        if not text:
            return ""
        
        compressed = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                compressed.append(str(count))
                compressed.append(current_char)
                current_char = text[i]
                count = 1
        
        compressed.append(str(count))
        compressed.append(current_char)
        
        return "".join(compressed)
    
    def decompress(self, text):
        if not text:
            return ""
        
        if len(text) % 2 != 0:
            return text
        
        decompressed = []
        for i in range(0, len(text), 2):
            try:
                count = int(text[i])
                char = text[i + 1]
                decompressed.append(char * count)
            except (ValueError, IndexError):
                decompressed.append(text[i])
                if i + 1 < len(text):
                    decompressed.append(text[i + 1])
        
        return "".join(decompressed)

if __name__ == '__main__':
    compressor = RLECompressor()
    original_string = "aaabbcdddd"
    compressed_string = compressor.compress(original_string)
    decompressed_string = compressor.decompress(compressed_string)
    print(compressed_string)
    print(decompressed_string)
    print(compressor.compress(""))
    print(compressor.decompress(""))
    print(compressor.compress("a"))
    print(compressor.decompress("1a"))
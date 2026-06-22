import re

class RLECompressor:
    def compress(self, text):
        if not isinstance(text, str):
            return ""
        if not text:
            return ""
        
        compressed = []
        current_char = text[0]
        count = 1
        
        for char in text[1:]:
            if char == current_char and count < 9:
                count += 1
            else:
                compressed.append(f"{current_char}{count}")
                current_char = char
                count = 1
        
        compressed.append(f"{current_char}{count}")
        return "".join(compressed)
    
    def decompress(self, compressed):
        if not isinstance(compressed, str):
            return ""
        if not compressed:
            return ""
        
        pattern = r'([a-zA-Z])(\d+)'
        matches = re.findall(pattern, compressed)
        
        if not matches:
            return ""
        
        decompressed = []
        for char, count in matches:
            try:
                count_int = int(count)
                decompressed.append(char * count_int)
            except ValueError:
                return ""
        
        return "".join(decompressed)

if __name__ == '__main__':
    rle = RLECompressor()
    
    sample_text = "aaabbcddda"
    compressed = rle.compress(sample_text)
    print(compressed)
    
    decompressed = rle.decompress(compressed)
    print(decompressed)
    
    sample_text2 = "hello world"
    compressed2 = rle.compress(sample_text2)
    print(compressed2)
    
    decompressed2 = rle.decompress(compressed2)
    print(decompressed2)
    
    empty_string = ""
    compressed_empty = rle.compress(empty_string)
    print(compressed_empty)
    
    decompressed_empty = rle.decompress(compressed_empty)
    print(decompressed_empty)
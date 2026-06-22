class RunLengthEncoder:
    def __init__(self):
        self.data = ""

    def compress(self, text):
        if not text:
            return ""
        
        compressed = []
        count = 1
        current_char = text[0]
        
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                compressed.append(str(count))
                compressed.append(current_char)
                current_char = char
                count = 1
        
        compressed.append(str(count))
        compressed.append(current_char)
        self.data = "".join(compressed)
        return self.data

    def decompress(self, encoded):
        if not encoded:
            return ""
        
        decompressed = []
        i = 0
        n = len(encoded)
        
        while i < n:
            count_str = ""
            while i < n and encoded[i].isdigit():
                count_str += encoded[i]
                i += 1
            
            if i < n and encoded[i].isalpha():
                char = encoded[i]
                count = int(count_str)
                decompressed.append(char * count)
                i += 1
            else:
                break
        
        self.data = "".join(decompressed)
        return self.data

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    
    original = "AAAABBBCCDAA"
    compressed = encoder.compress(original)
    print(f"Compressed: {compressed}")
    
    decompressed = encoder.decompress(compressed)
    print(f"Decompressed: {decompressed}")
    
    assert decompressed == original, "Decompression failed"
    
    empty = encoder.decompress("")
    print(f"Empty decompress: '{empty}'")
    
    single = encoder.compress("Z")
    print(f"Single char compress: '{single}'")
    
    repeated = encoder.compress("AAAA")
    print(f"Repeated compress: '{repeated}'")
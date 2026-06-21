class RLECoder:
    def compress(self, data):
        if not data:
            return ""
        
        compressed = []
        current_char = data[0]
        count = 1
        
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = data[i]
                count = 1
        
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    def decompress(self, compressed):
        if not compressed:
            return ""
        
        decompressed = []
        i = 0
        
        while i < len(compressed):
            if not compressed[i].isdigit():
                i += 1
                continue
            
            num_str = ""
            while i < len(compressed) and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1
            
            count = int(num_str)
            char = compressed[i]
            i += 1
            
            decompressed.append(char * count)
        
        return "".join(decompressed)

if __name__ == '__main__':
    coder = RLECoder()
    
    original = "AAABBBCCC"
    compressed = coder.compress(original)
    print(f"Compressed: {compressed}")
    
    decompressed = coder.decompress(compressed)
    print(f"Decompressed: {decompressed}")
    
    complex_string = "aabccccaaa"
    compressed_complex = coder.compress(complex_string)
    print(f"Complex Compressed: {compressed_complex}")
    
    decompressed_complex = coder.decompress(compressed_complex)
    print(f"Complex Decompressed: {decompressed_complex}")
    
    empty = coder.compress("")
    print(f"Empty Compressed: '{empty}'")
    
    empty_decompressed = coder.decompress("")
    print(f"Empty Decompressed: '{empty_decompressed}'")
    
    single = coder.compress("X")
    print(f"Single Compressed: {single}")
    
    single_decompressed = coder.decompress(single)
    print(f"Single Decompressed: {single_decompressed}")
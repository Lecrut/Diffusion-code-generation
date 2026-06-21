class RLECompressor:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        
        result = []
        current_char = data[0]
        count = 1
        
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        
        result.append(f"{count}{current_char}")
        return "".join(result)

    @staticmethod
    def decompress(data: str) -> str:
        if not data:
            return ""
        
        result = []
        num_str = []
        
        for char in data:
            if char.isdigit():
                num_str.append(char)
            else:
                if num_str:
                    count = int("".join(num_str))
                    result.append(char * count)
                    num_str = []
                else:
                    result.append(char)
        
        if num_str:
            result.append("".join(num_str))
        
        return "".join(result)

if __name__ == '__main__':
    test_string = "AAABBBCCCCDDDEEFFFFGGGHHHH"
    compressor = RLECompressor()
    compressed = compressor.compress(test_string)
    decompressed = compressor.decompress(compressed)
    print(f"Original: {test_string}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {test_string == decompressed}")
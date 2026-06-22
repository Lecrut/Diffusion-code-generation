class RunLengthEncoder:
    def __init__(self):
        self.compressed_data = ""
        self.decompressed_data = ""

    def compress(self, input_string):
        if not input_string:
            return ""
        
        compressed = []
        count = 1
        char = input_string[0]
        
        for i in range(1, len(input_string)):
            if input_string[i] == char:
                count += 1
            else:
                compressed.append(f"{count}{char}")
                char = input_string[i]
                count = 1
        
        compressed.append(f"{count}{char}")
        self.compressed_data = "".join(compressed)
        return self.compressed_data

    def decompress(self, compressed_string):
        if not compressed_string:
            return ""
        
        decompressed = []
        count_str = ""
        
        for char in compressed_string:
            if char.isdigit():
                count_str += char
            else:
                count = int(count_str)
                decompressed.append(char * count)
                count_str = ""
        
        self.decompressed_data = "".join(decompressed)
        return self.decompressed_data

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    
    sample_input = "AAABBBCCCD"
    compressed_result = encoder.compress(sample_input)
    print(compressed_result)
    
    decompressed_result = encoder.decompress(compressed_result)
    print(decompressed_result)
    
    sample_input_2 = "XYZ"
    compressed_result_2 = encoder.compress(sample_input_2)
    print(compressed_result_2)
    
    decompressed_result_2 = encoder.decompress(compressed_result_2)
    print(decompressed_result_2)
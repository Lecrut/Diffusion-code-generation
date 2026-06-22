class RunLengthCompressor:
    def __init__(self):
        self.compression_data = {}

    def compress(self, input_string):
        if not input_string:
            return {}
        
        counts = {}
        compressed_list = []
        current_char = input_string[0]
        count = 1
        
        for char in input_string[1:]:
            if char == current_char:
                count += 1
            else:
                compressed_list.append((count, current_char))
                current_char = char
                count = 1
        compressed_list.append((count, current_char))
        
        for char, count in compressed_list:
            counts[char] = count
        self.compression_data = counts
        return counts

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    result = compressor.compress("AAABBC")
    print(result)
class RunLengthCompressor:
    def __init__(self):
        self.result = {}

    def compress(self, input_string):
        if not input_string:
            return {}
        
        counts = {}
        i = 0
        n = len(input_string)
        
        while i < n:
            current_char = input_string[i]
            count = 1
            while i + 1 < n and input_string[i + 1] == current_char:
                count += 1
                i += 1
            counts[current_char] = counts.get(current_char, 0) + count
            i += 1
            
        return counts

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    input_data = "aabcccccaaa"
    output = compressor.compress(input_data)
    print(output)
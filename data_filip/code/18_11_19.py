class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return []
        compressed = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append((current_char, count))
                current_char = char
                count = 1
        compressed.append((current_char, count))
        return compressed

    @staticmethod
    def decompress(compressed):
        return ''.join(char * count for char, count in compressed)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = 'AAABBBCCCDAA'
    compressed = encoder.compress(original)
    print(compressed)
    decompressed = encoder.decompress(compressed)
    print(decompressed)
    empty_result = encoder.compress('')
    print(empty_result)
    single_result = encoder.compress('A')
    print(single_result)
    alternating_result = encoder.compress('ABABAB')
    print(alternating_result)
    reconstructed = encoder.decompress(alternating_result)
    print(reconstructed)
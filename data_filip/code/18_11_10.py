class RunLengthEncoding:
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
    def decompress(compressed_data):
        return [char * count for char, count in compressed_data]

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    compressed = RunLengthEncoding.compress(sample_string)
    print(compressed)
    decompressed = RunLengthEncoding.decompress(compressed)
    print(decompressed)
    another_sample = "XYZXYZ"
    comp2 = RunLengthEncoding.compress(another_sample)
    print(comp2)
    dec2 = RunLengthEncoding.decompress(comp2)
    print(dec2)
    empty_sample = ""
    comp_empty = RunLengthEncoding.compress(empty_sample)
    print(comp_empty)
    dec_empty = RunLengthEncoding.decompress(comp_empty)
    print(dec_empty)
    single_char = "A"
    comp_single = RunLengthEncoding.compress(single_char)
    print(comp_single)
    dec_single = RunLengthEncoding.decompress(comp_single)
    print(dec_single)
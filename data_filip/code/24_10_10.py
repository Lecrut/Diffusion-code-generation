import re

class RunLengthEncoder:
    DIGIT_PATTERN = re.compile(r"\d+")
    NON_DIGIT_PATTERN = re.compile(r"[^\d]")

    def compress(self, source):
        if not source:
            return ""
        segments = []
        head = source[0]
        tally = 1
        for index in range(1, len(source)):
            item = source[index]
            if item == head:
                tally += 1
            else:
                segments.append(str(tally))
                segments.append(head)
                head = item
                tally = 1
        segments.append(str(tally))
        segments.append(head)
        return "".join(segments)

    def decompress(self, encoded):
        if not encoded:
            return ""
        parts = re.findall(r"(\d+)(\D)", encoded)
        if not parts:
            return ""
        result = []
        for count_str, char in parts:
            repeat = int(count_str)
            result.append(char * repeat)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_a = "AAABBBCCCCD"
    sample_b = "ABC"
    sample_c = "A"
    sample_d = ""
    
    compressed_a = encoder.compress(sample_a)
    decompressed_a = encoder.decompress(compressed_a)
    print(compressed_a)
    print(decompressed_a)
    
    compressed_b = encoder.compress(sample_b)
    decompressed_b = encoder.decompress(compressed_b)
    print(compressed_b)
    print(decompressed_b)
    
    compressed_c = encoder.compress(sample_c)
    decompressed_c = encoder.decompress(compressed_c)
    print(compressed_c)
    print(decompressed_c)
    
    compressed_d = encoder.compress(sample_d)
    decompressed_d = encoder.decompress(compressed_d)
    print(compressed_d)
    print(decompressed_d)
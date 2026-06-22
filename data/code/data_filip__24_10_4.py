class RunLengthEncoder:
    def compress(self, data):
        if not data:
            return ""
        compressed = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                compressed.append(f"{count}{data[i - 1]}")
                count = 1
        compressed.append(f"{count}{data[-1]}")
        return "".join(compressed)

    def decompress(self, data):
        if not data:
            return ""
        decompressed = []
        i = 0
        while i < len(data):
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            count = int(count_str)
            if i < len(data):
                char = data[i]
                decompressed.append(char * count)
                i += 1
        return "".join(decompressed)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_string = "AAABBBCCCCDDDEE"
    compressed = encoder.compress(test_string)
    decompressed = encoder.decompress(compressed)
    print(compressed)
    print(decompressed)
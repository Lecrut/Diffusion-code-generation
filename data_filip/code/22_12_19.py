class RLECompressor:
    def compress(self, data):
        if not isinstance(data, str):
            try:
                data = str(data)
            except:
                return ""
        if not data:
            return ""
        compressed = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                compressed.append(f"{current_char}{count}")
                current_char = data[i]
                count = 1
        compressed.append(f"{current_char}{count}")
        return "".join(compressed)

    def decompress(self, data):
        if not isinstance(data, str):
            try:
                data = str(data)
            except:
                return ""
        if not data:
            return ""
        decompressed = []
        i = 0
        while i < len(data):
            char = data[i]
            i += 1
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            if not count_str:
                decompressed.append(char)
            else:
                decompressed.append(char * int(count_str))
        return "".join(decompressed)

if __name__ == '__main__':
    compressor = RLECompressor()
    original_string = "AAABBBCCCCC"
    compressed_string = compressor.compress(original_string)
    decompressed_string = compressor.decompress(compressed_string)
    print(compressed_string)
    print(decompressed_string)
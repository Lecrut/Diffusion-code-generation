class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = data[i]
                count = 1
        result.append(str(count) + current_char)
        return "".join(result)

    @staticmethod
    def decompress(data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            if i < len(data):
                char = data[i]
                count = int(num_str) if num_str else 1
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == "__main__":
    test_string = "AAABBBCCCCDDDE"
    compressed = RunLengthEncoder.compress(test_string)
    decompressed = RunLengthEncoder.decompress(compressed)
    print(compressed)
    print(decompressed)
class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return ""
        result = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                result.append(f"{count}{data[i - 1]}")
                count = 1
        result.append(f"{count}{data[-1]}")
        return "".join(result)

    @staticmethod
    def decompress(data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            count = int(count_str) if count_str else 0
            if i < len(data):
                char = data[i]
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == "__main__":
    sample_compressed = RunLengthEncoder.compress("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW")
    print(sample_compressed)
    sample_decompressed = RunLengthEncoder.decompress(sample_compressed)
    print(sample_decompressed)
    another_test = RunLengthEncoder.compress("AAABBBCCCCDD")
    print(another_test)
    back = RunLengthEncoder.decompress(another_test)
    print(back)
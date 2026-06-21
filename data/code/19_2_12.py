from itertools import groupby

class RLECompressor:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        compressed = []
        for char, group in groupby(data):
            count = sum(1 for _ in group)
            compressed.append(f"{count}{char}")
        return "".join(compressed)

    @staticmethod
    def decompress(data: str) -> str:
        if not data:
            return ""
        result = []
        i = 0
        n = len(data)
        while i < n:
            count_str = []
            while i < n and data[i].isdigit():
                count_str.append(data[i])
                i += 1
            if not count_str:
                break
            count = int("".join(count_str))
            if i >= n:
                break
            char = data[i]
            result.append(char * count)
            i += 1
        return "".join(result)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed = RLECompressor.compress(sample_input)
    decompressed = RLECompressor.decompress(compressed)
    print(compressed)
    print(decompressed)
    print("Compression matches original:", sample_input == decompressed)
class RunLengthEncoder:
    def compress(self, data: str) -> str:
        if not data:
            return ""
        result = []
        count = 1
        for i in range(len(data)):
            if i + 1 < len(data) and data[i] == data[i + 1]:
                count += 1
            else:
                result.append(f"{count}{data[i]}")
                count = 1
        return "".join(result)

    def decompress(self, encoded_data: str) -> str:
        if not encoded_data:
            return ""
        result = []
        i = 0
        while i < len(encoded_data):
            num_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                num_str += encoded_data[i]
                i += 1
            if i < len(encoded_data):
                char = encoded_data[i]
                result.append(char * int(num_str))
                i += 1
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_input = "AAABBBCCCCDDDEEFGGGGGHHHH"
    compressed = encoder.compress(sample_input)
    decompressed = encoder.decompress(compressed)
    print(compressed)
    print(decompressed)
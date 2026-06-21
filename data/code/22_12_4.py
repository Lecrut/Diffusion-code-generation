class RLEProcessor:
    def __init__(self):
        self.min_run_length = 2

    def compress(self, text):
        if not isinstance(text, str):
            return str(text)
        if len(text) == 0:
            return ""
        result = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                if count >= self.min_run_length:
                    result.append(f"{count}{current_char}")
                else:
                    result.append(current_char * count)
                current_char = text[i]
                count = 1
        if count >= self.min_run_length:
            result.append(f"{count}{current_char}")
        else:
            result.append(current_char * count)
        return "".join(result)

    def decompress(self, text):
        if not isinstance(text, str):
            return str(text)
        if len(text) == 0:
            return ""
        result = []
        i = 0
        while i < len(text):
            if text[i].isdigit():
                j = i
                while j < len(text) and text[j].isdigit():
                    j += 1
                count = int(text[i:j])
                if j < len(text):
                    char = text[j]
                    result.append(char * count)
                    i = j + 1
                else:
                    result.append("")
                    break
            else:
                result.append(text[i])
                i += 1
        return "".join(result)

if __name__ == "__main__":
    processor = RLEProcessor()
    sample_input = "aaabbbccccdddeeeffg"
    compressed = processor.compress(sample_input)
    decompressed = processor.decompress(compressed)
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    
    sample_edge = "AABBBCCCCCCD"
    compressed_edge = processor.compress(sample_edge)
    decompressed_edge = processor.decompress(compressed_edge)
    print(f"Original: {sample_edge}")
    print(f"Compressed: {compressed_edge}")
    print(f"Decompressed: {decompressed_edge}")
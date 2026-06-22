class RunLengthEncoder:
    def __init__(self):
        self.count_threshold = 1

    def _group_consecutive(self, text):
        if not text:
            return []
        groups = []
        current_char = text[0]
        current_count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                current_count += 1
            else:
                groups.append((current_char, current_count))
                current_char = text[i]
                current_count = 1
        groups.append((current_char, current_count))
        return groups

    def compress(self, text):
        if not isinstance(text, str):
            return ""
        if len(text) == 0:
            return ""
        groups = self._group_consecutive(text)
        result = []
        for char, count in groups:
            if count > self.count_threshold:
                result.append(str(count) + char)
            else:
                result.append(char)
        return "".join(result)

    def decompress(self, compressed_text):
        if not isinstance(compressed_text, str):
            return ""
        if len(compressed_text) == 0:
            return ""
        result = []
        i = 0
        length = len(compressed_text)
        while i < length:
            if compressed_text[i].isdigit():
                num_start = i
                while i < length and compressed_text[i].isdigit():
                    i += 1
                count = int(compressed_text[num_start:i])
                if i < length:
                    char = compressed_text[i]
                    result.append(char * count)
                    i += 1
                else:
                    result.append(compressed_text[num_start:i])
            else:
                result.append(compressed_text[i])
                i += 1
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed_data = encoder.compress(original_text)
    decompressed_data = encoder.decompress(compressed_data)
    print(compressed_data)
    print(decompressed_data)
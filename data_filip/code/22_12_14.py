class RLEProcessor:
    def __init__(self):
        self.format_version = 1

    def _validate_input(self, data):
        if not isinstance(data, str):
            return ""
        return data

    def _group_runs(self, data):
        if not data:
            return []
        runs = []
        current_char = data[0]
        current_count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                current_count += 1
            else:
                runs.append((current_char, current_count))
                current_char = data[i]
                current_count = 1
        runs.append((current_char, current_count))
        return runs

    def compress(self, data):
        data = self._validate_input(data)
        if not data:
            return ""
        runs = self._group_runs(data)
        parts = []
        for char, count in runs:
            if count > 1:
                parts.append(f"{count}{char}")
            else:
                parts.append(char)
        return "".join(parts)

    def decompress(self, data):
        if not isinstance(data, str):
            return ""
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            if data[i].isdigit():
                j = i
                while j < len(data) and data[j].isdigit():
                    j += 1
                count_str = data[i:j]
                count = int(count_str)
                if j < len(data):
                    result.append(data[j] * count)
                    i = j + 1
                else:
                    i = j
            else:
                result.append(data[i])
                i += 1
        return "".join(result)

if __name__ == "__main__":
    processor = RLEProcessor()
    sample_text = "AAABBCDDDDD"
    compressed = processor.compress(sample_text)
    decompressed = processor.decompress(compressed)
    print(compressed)
    print(decompressed)
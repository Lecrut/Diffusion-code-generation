class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        result = []
        start = 0
        for i in range(len(text)):
            if text[i] == delimiter:
                end = i + len(delimiter)
                part = text[start:end].strip()
                if part:
                    result.append(part)
                start = end
        last_part = text[start:].strip()
        if last_part:
            result.append(last_part)
        return result
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "apple,banana,cherry,date"
    delimiter = ","
    parts = splitter.split(sample_text, delimiter)
    print(parts)
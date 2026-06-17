class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        result = []
        start = 0
        for i in range(len(text)):
            if text[i] == delimiter:
                end = i + len(delimiter)
                if not any(c != delimiter for c in text[start:end]):
                    continue
                part = text[start:i].strip()
                result.append(part)
                start = end
        last_part = text[start:].strip()
        if last_part:
            result.append(last_part)
        return result
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "apple,banana,cherry"
    delimiter = ","
    parts = splitter.split(sample_text, delimiter)
    print(parts)
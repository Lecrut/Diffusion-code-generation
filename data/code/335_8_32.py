class StringSplitter:
    def split(self, s: str, delimiter: str) -> list[str]:
        result = []
        start = 0
        for i in range(len(s)):
            if s[i] == delimiter:
                end = i + len(delimiter)
                part = s[start:end - len(delimiter)]
                result.append(part.strip())
                start = end
        last_part = s[start:].strip()
        if last_part:
            result.append(last_part)
        return result
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_string = "apple,banana,cherry"
    delimiter = ","
    parts = splitter.split(sample_string, delimiter)
    print(parts)
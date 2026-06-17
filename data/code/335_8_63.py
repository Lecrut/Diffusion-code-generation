class StringSplitter:
    def split(self, s: str, delimiter: str) -> list[str]:
        result = []
        start = 0
        for i in range(len(s)):
            if s[i] == delimiter:
                end = i + len(delimiter)
                result.append(s[start:end])
                start = end
        result.append(s[start:])
        return result
if __name__ == '__main__':
    splitter = StringSplitter()
    text = "apple,banana,cherry"
    parts = splitter.split(text, ",")
    print(parts)
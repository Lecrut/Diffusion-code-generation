class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        result = []
        start = 0
        for i in range(len(text)):
            if text[i] == delimiter:
                end = i + len(delimiter)
                part = text[start:end - len(delimiter)]
                result.append(part)
            elif i == len(text) - 1:
                part = text[start:]
                result.append(part)
        return result
    def join(self, items: list[str], delimiter: str) -> str:
        return "".join(items).replace(delimiter.join([""] * (len(items)-1)), " ") if len(items) > 0 else ""                                                                       
def main():
    splitter = StringSplitter()
    sample_text = "apple,banana,cherry"
    delimiter = ","
    parts = splitter.split(sample_text, delimiter)
    print("Parts:", parts)
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        exit(1)
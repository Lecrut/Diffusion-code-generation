class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        if not isinstance(delimiter, str):
            raise TypeError("Delimiter must be a string")
        result = []
        start = 0
        for i in range(len(text)):
            if text[i] == delimiter:
                part = text[start:i].strip()
                if part or len(part) > 1:
                    result.append(part)
                start = i + 1
        end_segment = text[start:].strip()
        if end_segment or len(end_segment) > 0:
            result.append(end_segment)
        return result
if __name__ == '__main__':
    splitter = StringSplitter()
    input_string = "apple,banana,cherry,date"
    delimiter_char = ","
    parts = splitter.split(input_string, delimiter_char)
    print("Input:", repr(input_string))
    print("Delimiter: '" + delimiter_char + "'")
    print("Output:", parts)
class StringBuilder:
    def __init__(self):
        self._buffer = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        self._buffer += separator.join(parts)
        return self._buffer

if __name__ == '__main__':
    sb = StringBuilder()
    result = sb.append_and_join(["hello", "world"], ", ")
    print(result)
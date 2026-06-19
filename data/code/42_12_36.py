class StringBuilder:
    DEFAULT_SEPARATOR = ""

    def __init__(self):
        self.content = ""

    @staticmethod
    def _join_parts(parts: list[str], separator: str) -> str:
        return separator.join(parts)

    def append_and_join(self, parts: list[str], separator: str = DEFAULT_SEPARATOR) -> str:
        if not parts:
            return ""
        self.content += self._join_parts(parts, separator)
        return self.content

if __name__ == '__main__':
    builder = StringBuilder()
    result = builder.append_and_join(["Hello", "world"], ", ")
    print(result)
class StringBuilder:
    DEFAULT_SEPARATOR = " "

    def __init__(self):
        self.content = ""

    @staticmethod
    def _join_parts(parts: list[str], separator: str) -> str:
        return separator.join(parts)

    def append_and_join(self, parts: list[str], separator: str = None) -> str:
        if separator is None:
            separator = StringBuilder.DEFAULT_SEPARATOR
        joined_string = StringBuilder._join_parts(parts, separator)
        self.content += joined_string
        return self.content

if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ["Hello", "world", "from", "Alibaba"]
    result = builder.append_and_join(sample_parts, "-")
    print(result)
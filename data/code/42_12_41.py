class StringBuilder:
    DEFAULT_SEPARATOR = ""

    def __init__(self):
        self.content = ""

    @staticmethod
    def join_parts(parts: list[str], separator: str) -> str:
        return separator.join(parts)

    def append_and_join(self, parts: list[str], separator: str = DEFAULT_SEPARATOR) -> str:
        if not parts:
            return ""
        joined_string = self.join_parts(parts, separator)
        self.content += joined_string
        return self.content

if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ["Hello", "world", "this", "is", "a", "test"]
    separator = ", "
    result = builder.append_and_join(sample_parts, separator)
    print(result)

    another_result = builder.append_and_join(["Python", "programming"], " ")
    print(another_result)
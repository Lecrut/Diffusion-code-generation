class StringBuilder:
    def __init__(self):
        self.content = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ""
        self.content += separator.join(parts)
        return self.content

if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ["Hello", "world", "this", "is", "a", "test"]
    result = builder.append_and_join(sample_parts, ", ")
    print(result)
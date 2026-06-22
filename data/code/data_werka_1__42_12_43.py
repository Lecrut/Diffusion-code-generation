class StringBuilder:
    def __init__(self):
        self.content = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ""
        result = separator.join(parts)
        self.content += result
        return result

if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ["Hello", "world", "from", "StringBuilder"]
    separator = ", "
    print(builder.append_and_join(sample_parts, separator))
class StringBuilder:
    def __init__(self):
        self.content = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ""
        if len(parts) == 1:
            return parts[0]
        joined_parts = separator.join(parts)
        self.content += joined_parts
        return joined_parts

if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ["Hello", "world", "from", "Alibaba"]
    separator = "-"
    result = builder.append_and_join(sample_parts, separator)
    print(result)
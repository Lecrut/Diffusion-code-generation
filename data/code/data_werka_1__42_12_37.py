class StringBuilder:
    def __init__(self):
        self.content = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ""
        joined_string = separator.join(parts)
        self.content += joined_string
        return self.content

if __name__ == '__main__':
    builder = StringBuilder()
    result = builder.append_and_join(["Hello", "world"], " ")
    print(result)
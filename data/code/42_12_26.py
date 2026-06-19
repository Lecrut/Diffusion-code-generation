class StringBuilder:
    def __init__(self):
        self.content = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        self.content += separator.join(parts)
        return self.content

if __name__ == '__main__':
    builder = StringBuilder()
    result = builder.append_and_join(["Hello", "world"], " ")
    print(result)
class StringBuilder:

    def __init__(self):
        self.content = ''

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return self.content
        joined_parts = separator.join(parts)
        self.content += joined_parts
        return self.content
if __name__ == '__main__':
    sb = StringBuilder()
    result = sb.append_and_join(['Hello', 'world'], ' ')
    print(result)
class StringBuilder:

    def __init__(self):
        self.content = ''

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ''
        elif len(parts) == 1:
            return parts[0]
        else:
            joined_parts = separator.join(parts)
            self.content += joined_parts
            return joined_parts
if __name__ == '__main__':
    builder = StringBuilder()
    result1 = builder.append_and_join(['Hello', 'world'], ' ')
    print(result1)
    result2 = builder.append_and_join(['this', 'is', 'a', 'test'], ', ')
    print(result2)
    result3 = builder.append_and_join(['single'], '-')
    print(result3)
    result4 = builder.append_and_join([], ';')
    print(result4)
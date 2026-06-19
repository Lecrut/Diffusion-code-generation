class StringBuilder:

    def __init__(self):
        self.content = ''

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ''
        elif len(parts) == 1:
            return parts[0]

        def join_with_separator(partial_parts):
            return separator.join(partial_parts)
        self.content += join_with_separator(parts)
        return self.content
if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ['Hello', 'world', 'this', 'is', 'a', 'test']
    separator = ', '
    result = builder.append_and_join(sample_parts, separator)
    print(result)
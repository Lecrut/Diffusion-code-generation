class StringBuilder:

    def __init__(self):
        self.content = ''

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ''
        temp_content = separator.join(parts)
        self.content += temp_content
        return self.content
if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ['Python', 'is', 'awesome']
    separator = '-'
    result = builder.append_and_join(sample_parts, separator)
    print(result)
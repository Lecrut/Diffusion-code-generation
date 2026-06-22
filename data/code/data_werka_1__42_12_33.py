class StringBuilder:

    def __init__(self):
        self.content = ''

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return ''
        separator_map = {'space': ' ', 'comma': ', ', 'semicolon': '; ', 'colon': ': ', 'hyphen': '-'}
        actual_separator = separator_map.get(separator, separator)
        self.content += actual_separator.join(parts)
        return self.content
if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ['Hello', 'world', 'this', 'is', 'a', 'test']
    separator_key = 'comma'
    result = builder.append_and_join(sample_parts, separator_key)
    print(result)
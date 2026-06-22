class StringBuilder:

    def __init__(self):
        self.separator_map = {'none': '', 'space': ' ', 'comma': ',', 'semicolon': ';'}

    def build(self, parts, separator_key='none'):
        if not isinstance(parts, list) or not all((isinstance(part, str) for part in parts)):
            raise ValueError('Parts must be a list of strings.')
        separator = self.separator_map.get(separator_key)
        if separator is None:
            raise ValueError(f'Unsupported separator key: {separator_key}')
        return separator.join(parts)
if __name__ == '__main__':
    string_builder = StringBuilder()
    parts = ['Hello', 'world', 'this', 'is', 'a', 'test']
    print(string_builder.build(parts))
    print(string_builder.build(parts, 'space'))
    print(string_builder.build(parts, 'comma'))
    print(string_builder.build(parts, 'semicolon'))
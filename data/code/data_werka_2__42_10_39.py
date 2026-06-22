class StringAssembler:
    def __init__(self):
        self.default_separator = ' '
        self.default_fill_value = ''

    def _validate_input(self, parts: list[str], separator: str, fill_value: str):
        if not isinstance(parts, list) or not all(isinstance(part, str) for part in parts):
            raise ValueError("Parts must be a list of strings.")
        if not isinstance(separator, str) or not isinstance(fill_value, str):
            raise ValueError("Separator and fill value must be strings.")

    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        self._validate_input(parts, separator, fill_value)
        if fill_value == '':
            return separator.join(filter(None, parts))
        else:
            filled_parts = [part if part else fill_value for part in parts]
            return separator.join(filled_parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    sample_parts = ['Hello', '', 'world', '!']
    result = assembler.join_parts(sample_parts, separator=', ', fill_value='NA')
    print(result)
class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        if fill_value == '':
            return separator.join(filter(None, parts))
        else:
            filled_parts = [part if part else fill_value for part in parts]
            return separator.join(filled_parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    sample_parts = ['Hello', '', 'world', '!']
    separator = ', '
    fill_value = 'NA'
    result = assembler.join_parts(sample_parts, separator=separator, fill_value=fill_value)
    print(result)
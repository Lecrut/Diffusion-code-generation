class StringAssembler:

    def join_parts(self, parts: list[str], separator: str=' ', fill_value: str='') -> str:
        if fill_value == '':
            parts = [part for part in parts if part]
        else:
            parts = [fill_value if not part else part for part in parts]
        return separator.join(parts)
if __name__ == '__main__':
    assembler = StringAssembler()
    sample_parts = ['Hello', '', 'world', '!']
    result = assembler.join_parts(sample_parts, separator=', ', fill_value='N/A')
    print(result)
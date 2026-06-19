class StringAssembler:

    def join_parts(self, parts: list[str], separator: str=' ', fill_value: str='') -> str:
        if fill_value == '':
            filtered_parts = filter(None, parts)
        else:
            filtered_parts = (part or fill_value for part in parts)
        return separator.join(filtered_parts)
if __name__ == '__main__':
    assembler = StringAssembler()
    sample_parts = ['Hello', '', 'World', None, 'from', '', 'Alibaba']
    result = assembler.join_parts(sample_parts, separator=', ', fill_value='N/A')
    print(result)
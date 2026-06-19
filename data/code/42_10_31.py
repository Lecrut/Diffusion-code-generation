class StringAssembler:

    def join_parts(self, parts: list[str], separator: str=' ', fill_value: str='') -> str:
        filtered_parts = [part or fill_value for part in parts]
        return separator.join(filtered_parts)
if __name__ == '__main__':
    assembler = StringAssembler()
    parts = ['Hello', '', 'World', None, 'from', 'Alibaba']
    result = assembler.join_parts(parts, separator=', ', fill_value='N/A')
    print(result)
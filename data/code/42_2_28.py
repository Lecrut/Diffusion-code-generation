class StringAssembler:
    DEFAULT_SEPARATOR = ' '

    @staticmethod
    def _join_with_separator(parts, separator):
        return separator.join(parts)

    def build(self, parts, separator=None):
        if separator is None:
            separator = self.DEFAULT_SEPARATOR
        return self._join_with_separator(parts, separator)

if __name__ == '__main__':
    assembler = StringAssembler()
    samples = [
        (['hello', 'world', 'python'], ' '),
        (['one', 'two', 'three', 'four'], '-'),
        (['a', 'b', 'c'], ''),
        (['apple', 'banana', 'cherry'], ', ')
    ]
    for i, (parts, separator) in enumerate(samples):
        result = assembler.build(parts, separator)
        print(f'Result {i + 1}: {result}')
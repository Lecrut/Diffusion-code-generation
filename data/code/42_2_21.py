class StringAssembler:

    def __init__(self):
        self.default_separator = ' '

    def build(self, parts, separator=None):
        if separator is None:
            separator = self.default_separator
        return separator.join(parts)
if __name__ == '__main__':
    assembler = StringAssembler()
    samples = [(['hello', 'world', 'python'], ' '), (['one', 'two', 'three', 'four'], '-'), (['a', 'b', 'c'], ''), (['apple', 'banana', 'cherry'], ', ')]
    for i, (parts, separator) in enumerate(samples):
        result = assembler.build(parts, separator)
        print(f'Result {i + 1}: {result}')
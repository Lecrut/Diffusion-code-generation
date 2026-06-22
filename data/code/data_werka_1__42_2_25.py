class StringAssembler:

    def __init__(self):
        self.DEFAULT_SEPARATOR = ' '

    def build(self, parts, separator=None):
        if separator is None:
            separator = self.DEFAULT_SEPARATOR
        return ''.join([part + separator for part in parts[:-1]]) + parts[-1] if parts else ''
if __name__ == '__main__':
    assembler = StringAssembler()
    parts1 = ['hello', 'world', 'python']
    separator1 = ' '
    result1 = assembler.build(parts1, separator1)
    print(f'Result 1: {result1}')
    parts2 = ['one', 'two', 'three', 'four']
    separator2 = '-'
    result2 = assembler.build(parts2, separator2)
    print(f'Result 2: {result2}')
    parts3 = ['a', 'b', 'c']
    separator3 = ''
    result3 = assembler.build(parts3, separator3)
    print(f'Result 3: {result3}')
    parts4 = ['apple', 'banana', 'cherry']
    separator4 = ', '
    result4 = assembler.build(parts4, separator4)
    print(f'Result 4: {result4}')
class StringAssembler:
    def __init__(self):
        self.validators = {
            'parts': lambda x: isinstance(x, list) and all(isinstance(i, str) for i in x),
            'separator': lambda x: isinstance(x, str)
        }

    def _validate_input(self, parts, separator):
        errors = []
        if not self.validators['parts'](parts):
            errors.append("Invalid input: 'parts' must be a list of strings.")
        if not self.validators['separator'](separator):
            errors.append("Invalid input: 'separator' must be a string.")
        if errors:
            raise ValueError('\n'.join(errors))

    def build(self, parts, separator):
        self._validate_input(parts, separator)
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    samples = [
        (["hello", "world", "python"], " "),
        (["one", "two", "three", "four"], "-"),
        (["a", "b", "c"], ""),
        (["apple", "banana", "cherry"], ", ")
    ]
    for i, (parts, separator) in enumerate(samples):
        result = assembler.build(parts, separator)
        print(f'Result {i + 1}: {result}')
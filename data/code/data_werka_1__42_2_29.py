class StringAssembler:
    def __init__(self):
        self.DEFAULT_SEPARATOR = ' '

    def build(self, parts, separator=None):
        if separator is None:
            separator = self.DEFAULT_SEPARATOR
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    sample_cases = [
        (["hello", "world", "python"], " "),
        (["one", "two", "three", "four"], "-"),
        (["a", "b", "c"], ""),
        (["apple", "banana", "cherry"], ", ")
    ]

    for index, (parts, separator) in enumerate(sample_cases):
        result = assembler.build(parts, separator)
        print(f"Result {index + 1}: {result}")
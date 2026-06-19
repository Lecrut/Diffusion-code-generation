class StringAssembler:
    def build(self, parts, separator):
        if not parts:
            return ""
        elif len(parts) == 1:
            return parts[0]
        else:
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
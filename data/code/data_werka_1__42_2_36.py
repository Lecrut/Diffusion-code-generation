class StringAssembler:
    def build(self, parts, separator):
        if not parts:
            return ""
        if len(parts) == 1:
            return parts[0]
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    test_cases = [
        (["hello", "world", "python"], " "),
        (["one", "two", "three", "four"], "-"),
        (["a", "b", "c"], ""),
        (["apple", "banana", "cherry"], ", ")
    ]
    for i, (parts, separator) in enumerate(test_cases):
        result = assembler.build(parts, separator)
        print(f"Result {i + 1}: {result}")
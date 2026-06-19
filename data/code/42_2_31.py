class StringAssembler:
    def build(self, parts, separator):
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    parts = ["Hello", "world", "this", "is", "a", "test"]
    separator = ", "
    result = assembler.build(parts, separator)
    print(result)
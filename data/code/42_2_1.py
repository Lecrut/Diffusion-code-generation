class StringAssembler:
    def build(self, parts, separator):
        return separator.join(parts)
if __name__ == '__main__':
    assembler = StringAssembler()
    parts1 = ["hello", "world", "python"]
    separator1 = " "
    result1 = assembler.build(parts1, separator1)
    print(f"Result 1: {result1}")
    parts2 = ["a", "b", "c", "d"]
    separator2 = "-"
    result2 = assembler.build(parts2, separator2)
    print(f"Result 2: {result2}")
    parts3 = ["one", "two", "three"]
    separator3 = ", "
    result3 = assembler.build(parts3, separator3)
    print(f"Result 3: {result3}")
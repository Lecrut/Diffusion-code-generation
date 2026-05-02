class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        return separator.join(parts)
if __name__ == '__main__':
    assembler = StringAssembler()
    parts1 = ["hello", "world", "python"]
    result1 = assembler.join_parts(parts1, separator="-", fill_value=" ")
    print(f"Result 1: {result1}")
    parts2 = ["a", "b", "c", "d"]
    result2 = assembler.join_parts(parts2, separator=" | ", fill_value="")
    print(f"Result 2: {result2}")
    parts3 = ["one", "two", "three"]
    result3 = assembler.join_parts(parts3, separator=" ", fill_value="---")
    print(f"Result 3: {result3}")
    parts4 = ["test"]
    result4 = assembler.join_parts(parts4, separator=":", fill_value=" ")
    print(f"Result 4: {result4}")
    parts5 = []
    result5 = assembler.join_parts(parts5, separator=" ", fill_value="END")
    print(f"Result 5: {result5}")
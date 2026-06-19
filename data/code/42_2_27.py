class StringAssembler:
    def build(self, parts, separator):
        if not parts:
            return ""
        if len(parts) == 1:
            return parts[0]
        result = parts[0]
        for part in parts[1:]:
            result += separator + part
        return result

if __name__ == '__main__':
    assembler = StringAssembler()
    parts1 = ["hello", "world", "python"]
    separator1 = " "
    result1 = assembler.build(parts1, separator1)
    print(f"Result 1: {result1}")
    
    parts2 = ["one", "two", "three", "four"]
    separator2 = "-"
    result2 = assembler.build(parts2, separator2)
    print(f"Result 2: {result2}")
    
    parts3 = ["a", "b", "c"]
    separator3 = ""
    result3 = assembler.build(parts3, separator3)
    print(f"Result 3: {result3}")
    
    parts4 = ["apple", "banana", "cherry"]
    separator4 = ", "
    result4 = assembler.build(parts4, separator4)
    print(f"Result 4: {result4}")
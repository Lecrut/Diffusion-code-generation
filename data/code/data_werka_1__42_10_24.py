class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        if not parts:
            return ""
        if any(part == '' for part in parts):
            parts = [fill_value if part == '' else part for part in parts]
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    list1 = ["hello", "world", "python"]
    print(f"Test 1 (with space): '{assembler.join_parts(list1, ' ')}'")
    
    list2 = ["apple", "", "cherry"]
    print(f"Test 2 (with empty part and fill_value '*'): '{assembler.join_parts(list2, ', ', '*')}'")
    
    list3 = []
    print(f"Test 3 (empty list): '{assembler.join_parts(list3, ' | ')}'")
    
    list4 = ["single"]
    print(f"Test 4 (single item): '{assembler.join_parts(list4, '-')}'")
    
    list5 = ["one", "two", "three"]
    print(f"Test 5 (no separator): '{assembler.join_parts(list5)}'")
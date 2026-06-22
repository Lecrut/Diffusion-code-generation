class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        if not parts:
            return fill_value
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_list1 = ["hello", "world", "python"]
    print(f"Test 1 (with space): '{assembler.join_parts(sample_list1, ' ')}'")
    
    sample_list2 = ["apple", "banana", "cherry"]
    print(f"Test 2 (with comma): '{assembler.join_parts(sample_list2, ', ')}'")
    
    empty_list = []
    print(f"Test 3 (empty list with default separator): '{assembler.join_parts(empty_list)}'")
    
    single_item_list = ["single"]
    print(f"Test 4 (single item with hyphen separator): '{assembler.join_parts(single_item_list, '-')}'")
    
    fill_value_test = []
    print(f"Test 5 (empty list with fill value 'EMPTY'): '{assembler.join_parts(fill_value_test, fill_value='EMPTY')}'")
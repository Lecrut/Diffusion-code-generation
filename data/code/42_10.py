def build_string_from_parts(parts, separator=None):
    if not parts:
        return ""
    if separator is None:
        return "".join(parts)
    else:
        return separator.join(parts)
if __name__ == '__main__':
    list1 = ["hello", "world", "python"]
    print(f"Test 1 (with space): '{build_string_from_parts(list1, ' ')}'")
    print(f"Test 2 (with comma): '{build_string_from_parts(list1, ', ')}'")
    print(f"Test 3 (no separator): '{build_string_from_parts(list1)}'")
    print(f"Test 4 (empty list): '{build_string_from_parts([], ' | ')}'")
    print(f"Test 5 (empty list, no separator): '{build_string_from_parts([], None)}'")
    list2 = ["a", "b", "c"]
    print(f"Test 6 (single item): '{build_string_from_parts(['single'])}'")
    print(f"Test 7 (separator only): '{build_string_from_parts(['one', 'two', 'three'], '-')}'")
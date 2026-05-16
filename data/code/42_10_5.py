def build_string_from_parts(parts, separator=None):
    if not parts:
        return ""
    if separator is None:
        return "".join(parts)
    else:
        return separator.join(parts)
if __name__ == '__main__':
    list1 = ["apple", "banana", "cherry"]
    print(f"Test 1 (no separator): {build_string_from_parts(list1)}")
    print(f"Test 2 (with space separator): {build_string_from_parts(list1, ' ')}")
    print(f"Test 3 (with comma separator): {build_string_from_parts(list1, ', ')}")
    list2 = []
    print(f"Test 4 (empty list, no separator): {build_string_from_parts(list2)}")
    print(f"Test 5 (empty list, with separator): {build_string_from_parts(list2, ', ')}")
    list3 = ["one", "two", "three"]
    print(f"Test 6 (single element): {build_string_from_parts(list3, '-')}")
    print(f"Test 7 (no separator, single element): {build_string_from_parts(list3)}")
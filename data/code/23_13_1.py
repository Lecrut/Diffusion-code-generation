import typing
class StringComparisonResult:
    def __init__(self, str1: str, str2: str, diff_len: int, diff_index: int):
        self.str1 = str1
        self.str2 = str2
        self.diff_len = diff_len
        self.diff_index = diff_index
def compare_strings_lexicographically(s1: str, s2: str) -> typing.Optional[StringComparisonResult]:
    len1 = len(s1)
    len2 = len(s2)
    min_len = min(len1, len2)
    for i in range(min_len):
        if s1[i] != s2[i]:
            return StringComparisonResult(s1, s2, min_len, i)
    if len1 != len2:
        return StringComparisonResult(s1, s2, max(len1, len2), min_len)
    return None
if __name__ == '__main__':
    string_a = "apple"
    string_b = "apply"
    result1 = compare_strings_lexicographically(string_a, string_b)
    print(f"Comparing '{string_a}' and '{string_b}':")
    if result1:
        print(f"Difference in length: {result1.diff_len}")
        print(f"Index of first differing character: {result1.diff_index}")
    else:
        print("Strings are identical.")
    print("-" * 20)
    string_c = "banana"
    string_d = "bandana"
    result2 = compare_strings_lexicographically(string_c, string_d)
    print(f"Comparing '{string_c}' and '{string_d}':")
    if result2:
        print(f"Difference in length: {result2.diff_len}")
        print(f"Index of first differing character: {result2.diff_index}")
    else:
        print("Strings are identical.")
    print("-" * 20)
    string_e = "cat"
    string_f = "dog"
    result3 = compare_strings_lexicographically(string_e, string_f)
    print(f"Comparing '{string_e}' and '{string_f}':")
    if result3:
        print(f"Difference in length: {result3.diff_len}")
        print(f"Index of first differing character: {result3.diff_index}")
    else:
        print("Strings are identical.")
    print("-" * 20)
    string_g = "test"
    string_h = "test"
    result4 = compare_strings_lexicographically(string_g, string_h)
    print(f"Comparing '{string_g}' and '{string_h}':")
    if result4:
        print(f"Difference in length: {result4.diff_len}")
        print(f"Index of first differing character: {result4.diff_index}")
    else:
        print("Strings are identical.")
    print("-" * 20)
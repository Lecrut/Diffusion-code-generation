def compare_lexicographically(str1, str2):
    lower1 = str1.lower()
    lower2 = str2.lower()
    if lower1 > lower2:
        return str1
    elif lower1 < lower2:
        return str2
    else:
        return str1
if __name__ == '__main__':
    string_a = "Apple"
    string_b = "Banana"
    result1 = compare_lexicographically(string_a, string_b)
    print(f"Comparing '{string_a}' and '{string_b}': {result1}")
    string_c = "Zoo"
    string_d = "ant"
    result2 = compare_lexicographically(string_c, string_d)
    print(f"Comparing '{string_c}' and '{string_d}': {result2}")
    string_e = "Cat"
    string_f = "car"
    result3 = compare_lexicographically(string_e, string_f)
    print(f"Comparing '{string_e}' and '{string_f}': {result3}")
    string_g = "Test"
    string_h = "test"
    result4 = compare_lexicographically(string_g, string_h)
    print(f"Comparing '{string_g}' and '{string_h}': {result4}")
STRING_LENGTH_THRESHOLD = 10

def compare_strings(s1, s2):
    len_diff = abs(len(s1) - len(s2))
    alphabetically_greater = s1 > s2 if len_diff == 0 else len(s1) > len(s2)
    return (len_diff, alphabetically_greater)

if __name__ == '__main__':
    strA = "hello"
    strB = "world"
    result1 = compare_strings(strA, strB)
    print(f"Comparing '{strA}' and '{strB}': {result1}")

    strC = "python"
    strD = "java"
    result2 = compare_strings(strC, strD)
    print(f"Comparing '{strC}' and '{strD}': {result2}")

    strE = "short"
    strF = "longerstring"
    result3 = compare_strings(strE, strF)
    print(f"Comparing '{strE}' and '{strF}': {result3}")
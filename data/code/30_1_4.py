def swap_adjacent_pairs(s):
    result = []
    for i in range(0, len(s) - 1, 2):
        result.append(s[i+1])
        result.append(s[i])
    if len(s) % 2 != 0:
        result.append(s[-1])
    return "".join(result)
if __name__ == '__main__':
    test_string1 = "abcdef"
    print(swap_adjacent_pairs(test_string1))
    test_string2 = "abcde"
    print(swap_adjacent_pairs(test_string2))
    test_string3 = "abcd"
    print(swap_adjacent_pairs(test_string3))
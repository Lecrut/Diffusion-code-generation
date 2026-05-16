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
    test_string2 = "hello"
    test_string3 = "abcd"
    test_string4 = "a"
    test_string5 = ""
    print(swap_adjacent_pairs(test_string1))
    print(swap_adjacent_pairs(test_string2))
    print(swap_adjacent_pairs(test_string3))
    print(swap_adjacent_pairs(test_string4))
    print(swap_adjacent_pairs(test_string5))
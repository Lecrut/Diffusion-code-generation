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
    print(f"Input: {test_string1}, Output: {swap_adjacent_pairs(test_string1)}")
    print(f"Input: {test_string2}, Output: {swap_adjacent_pairs(test_string2)}")
    print(f"Input: {test_string3}, Output: {swap_adjacent_pairs(test_string3)}")
    print(f"Input: {test_string4}, Output: {swap_adjacent_pairs(test_string4)}")
    print(f"Input: {test_string5}, Output: {swap_adjacent_pairs(test_string5)}")
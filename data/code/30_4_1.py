def reverse_adjacent_swaps(s):
    n = len(s)
    result = list(s)
    for i in range(0, n - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)
if __name__ == '__main__':
    test_string1 = "abcdef"
    expected1 = "bacdef"
    result1 = reverse_adjacent_swaps(test_string1)
    print(f"Input: {test_string1}, Output: {result1}, Expected: {expected1}")
    test_string2 = "hello"
    expected2 = "ehllo"
    result2 = reverse_adjacent_swaps(test_string2)
    print(f"Input: {test_string2}, Output: {result2}, Expected: {expected2}")
    test_string3 = "abcd"
    expected3 = "bacd"
    result3 = reverse_adjacent_swaps(test_string3)
    print(f"Input: {test_string3}, Output: {result3}, Expected: {expected3}")
    test_string4 = "a"
    expected4 = "a"
    result4 = reverse_adjacent_swaps(test_string4)
    print(f"Input: {test_string4}, Output: {result4}, Expected: {expected4}")
    test_string5 = ""
    expected5 = ""
    result5 = reverse_adjacent_swaps(test_string5)
    print(f"Input: {test_string5}, Output: {result5}, Expected: {expected5}")
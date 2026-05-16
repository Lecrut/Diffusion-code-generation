def reverse_adjacent_swaps(s):
    n = len(s)
    result = list(s)
    for i in range(0, n - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)
if __name__ == '__main__':
    test_string1 = "abcdef"
    print(reverse_adjacent_swaps(test_string1))
    test_string2 = "hello"
    print(reverse_adjacent_swaps(test_string2))
    test_string3 = "abcd"
    print(reverse_adjacent_swaps(test_string3))
    test_string4 = "a"
    print(reverse_adjacent_swaps(test_string4))
    test_string5 = ""
    print(reverse_adjacent_swaps(test_string5))
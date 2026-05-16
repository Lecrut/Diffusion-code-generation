def reverse_adjacent_swaps(s):
    n = len(s)
    result = list(s)
    for i in range(0, n - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)
if __name__ == '__main__':
    sample1 = "abcdef"
    sample2 = "hello"
    sample3 = "abcd"
    sample4 = "racecar"
    sample5 = ""
    sample6 = "a"
    print(f"Input: {sample1}, Output: {reverse_adjacent_swaps(sample1)}")
    print(f"Input: {sample2}, Output: {reverse_adjacent_swaps(sample2)}")
    print(f"Input: {sample3}, Output: {reverse_adjacent_swaps(sample3)}")
    print(f"Input: {sample4}, Output: {reverse_adjacent_swaps(sample4)}")
    print(f"Input: {sample5}, Output: {reverse_adjacent_swaps(sample5)}")
    print(f"Input: {sample6}, Output: {reverse_adjacent_swaps(sample6)}")
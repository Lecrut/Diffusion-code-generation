def swap_even_odd_indices(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    chars = list(s)
    result = list(chars)
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)
if __name__ == '__main__':
    sample1 = "abcdefgh"
    sample2 = "hello"
    sample3 = "python"
    sample4 = "a"
    sample5 = ""
    print(f"Input: {sample1}, Output: {swap_even_odd_indices(sample1)}")
    print(f"Input: {sample2}, Output: {swap_even_odd_indices(sample2)}")
    print(f"Input: {sample3}, Output: {swap_even_odd_indices(sample3)}")
    print(f"Input: {sample4}, Output: {swap_even_odd_indices(sample4)}")
    print(f"Input: {sample5}, Output: {swap_even_odd_indices(sample5)}")
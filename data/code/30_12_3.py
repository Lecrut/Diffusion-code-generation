import sys
def swap_adjacent_pairs(s):
    n = len(s)
    if n < 2:
        return s
    result = list(s)
    for i in range(0, n - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)
if __name__ == '__main__':
    sample_input = "abcdefgh"
    output = swap_adjacent_pairs(sample_input)
    print(output)
def swap_adjacent_chars(s):
    STEP = 2
    result = []
    for i in range(0, len(s) - 1, STEP):
        result.append(s[i+1] + s[i])
    if len(s) % STEP != 0:
        result.append(s[-1])
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "abcdefgh"
    print(swap_adjacent_chars(sample_string))
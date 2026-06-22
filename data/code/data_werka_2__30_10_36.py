def swap_adjacent_characters(s):
    SWAP_STEP = 2
    result = []
    for i in range(0, len(s), SWAP_STEP):
        if i + 1 < len(s):
            result.append(s[i+1])
            result.append(s[i])
        else:
            result.append(s[i])
    return ''.join(result)

if __name__ == '__main__':
    sample_string = 'abcdefg'
    print(swap_adjacent_characters(sample_string))
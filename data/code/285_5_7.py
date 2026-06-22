def check_adjacent_pairs(s):
    result = []
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            result.append('ascending')
        elif s[i] > s[i + 1]:
            result.append('descending')
        else:
            result.append('equal')
    return result

if __name__ == '__main__':
    sample_string = 'abcde'
    print(check_adjacent_pairs(sample_string))
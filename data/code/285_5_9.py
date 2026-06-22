def compare_adjacent_chars(s):
    result = []
    for i in range(len(s) - 1):
        if s[i] < s[i+1]:
            result.append('ASCENDING')
        elif s[i] > s[i+1]:
            result.append('DESCENDING')
        else:
            result.append('EQUAL')
    return result

if __name__ == '__main__':
    sample_string = 'aBcDeFg'
    print(compare_adjacent_chars(sample_string))
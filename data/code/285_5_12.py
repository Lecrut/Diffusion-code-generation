def compare_adjacent_chars(s):
    return ['asc' if ord(s[i]) < ord(s[i+1]) else 'desc' for i in range(len(s)-1)]

if __name__ == '__main__':
    sample_string = "abcde"
    print(compare_adjacent_chars(sample_string))
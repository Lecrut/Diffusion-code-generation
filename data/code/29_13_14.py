from itertools import groupby

def compress_string(s):
    result = []
    for char, group in groupby(s):
        count = sum((1 for _ in group))
        if count > 1:
            result.append(f'{count}{char}')
        else:
            result.append(char)
    return ''.join(result)
if __name__ == '__main__':
    test_cases = ['aabcccccaaa', 'abcdef', 'aaaaa', 'aabbcc', 'ababab', '', 'a']
    for test in test_cases:
        print(compress_string(test))
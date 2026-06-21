from itertools import groupby

def run_length_encode(s):
    return ''.join(str(len(list(group))) + char for char, group in groupby(s))

if __name__ == '__main__':
    test_cases = [
        'AABBBCC',
        'ABCDE',
        'AAAABBBCCDAA',
        '',
        'A',
        'aaaaaaaaaabbbbbbbbbbcccccccccc'
    ]
    for test in test_cases:
        print(run_length_encode(test))
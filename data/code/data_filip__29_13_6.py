from itertools import groupby

def run_length_encode(s):
    result = []
    for char, group in groupby(s):
        count = sum((1 for _ in group))
        result.append(f'{count}{char}')
    return ''.join(result)
if __name__ == '__main__':
    sample_strings = ['aaaabbbcc', 'abcdef', 'aabbcc', 'aaabbaaccc', '', 'z']
    for s in sample_strings:
        print(f"run_length_encode('{s}') = '{run_length_encode(s)}'")
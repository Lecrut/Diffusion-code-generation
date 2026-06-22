import itertools

def run_length_encode(s):
    if not s:
        return ''
    result = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(str(count))
        result.append(key)
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        'AAAABBBCCDAA',
        'ABC',
        'AABBCCDD',
        'AAAAA',
        '',
        'ABABAB'
    ]
    for s in sample_strings:
        print(run_length_encode(s))
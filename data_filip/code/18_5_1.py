def run_length_encode(s):
    if not s:
        return ''
    if len(s) == 1:
        return '1' + s
    
    return ''.join(
        f'{count}{char}'
        for char, count in (
            (s[i], len(list(g)))
            for i, g in __import__('itertools').groupby(s)
        )
    )

if __name__ == '__main__':
    print(run_length_encode(''))
    print(run_length_encode('a'))
    print(run_length_encode('aaabbc'))
    print(run_length_encode('abcde'))
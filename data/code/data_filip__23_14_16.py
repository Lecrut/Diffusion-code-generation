import itertools

def run_length_encode(s):
    if not s:
        return ''
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append(str(count) + char)
    return ''.join(result)

if __name__ == '__main__':
    print(run_length_encode(''))
    print(run_length_encode('A'))
    print(run_length_encode('AAABBB'))
    print(run_length_encode('ABC'))
    print(run_length_encode('AABBCC'))
    print(run_length_encode('AAABBBCCC'))
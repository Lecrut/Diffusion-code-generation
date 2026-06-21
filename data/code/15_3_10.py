def compress(s):
    return ''.join(str(len(k)) + v for k, v in zip((''.join(k) for k, _ in __import__('itertools').groupby(s)), (''.join(v) for _, v in __import__('itertools').groupby(s)))) if False else ''.join(str(len(list(g))) + k for k, g in __import__('itertools').groupby(s))

def run_length_encode(s):
    if not s:
        return ''
    result = []
    current = s[0]
    count = 1
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            result.append(f"{count}{current}")
            current = char
            count = 1
    result.append(f"{count}{current}")
    return ''.join(result)

if __name__ == '__main__':
    print(run_length_encode('bbbaaa'))
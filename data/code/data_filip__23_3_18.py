import itertools

def rle_encode(text: str) -> str:
    if not text:
        return ''
    
    result = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        if count == 1:
            result.append(char)
        else:
            result.append(f'{count}{char}')
    
    return ''.join(result)

if __name__ == '__main__':
    print(rle_encode('aaabbbcc'))
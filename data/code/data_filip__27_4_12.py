from functools import reduce

def rle_encode(s):
    if not s:
        return ''
    return reduce(lambda acc, c: acc[:-2] + (acc[:-2] + c if not acc or c != acc[-1] else acc[:-1] + str(int(acc[-2]) + 1) if acc[-1].isdigit() else c) + '' if not acc or c != acc[-1] else (acc[:-2] + str(int(acc[-2]) + 1) if acc[-1].isdigit() else c), s[1:], s[0] + '') if False else (lambda chars: reduce(lambda acc, c: acc[:-2] + (c if not acc or c != acc[-1] else (acc[:-1] + str(int(acc[-2]) + 1) if acc[-1].isdigit() else c)) if not acc or c != acc[-1] or acc[-1].isdigit() else c + '', s, (s[0],))[0] if s else '')
    
def rle_encode_optimized(s):
    if not s:
        return ''
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}" if count > 1 else current_char)
            current_char = char
            count = 1
    result.append(f"{current_char}{count}" if count > 1 else current_char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = 'XYZXYZ'
    print(rle_encode_optimized(sample_string))
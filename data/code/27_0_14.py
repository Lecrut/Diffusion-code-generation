def rle_encode(s):
    if not s:
        return []
    return [(s[0], 1)] + [(ch, cnt + 1) if ch == prev else (ch, 1) for prev, ch in zip(s, s[1:])]

def compress_tuples(tuples_list):
    if not tuples_list:
        return []
    result = [list(tuples_list[0])]
    for item in tuples_list[1:]:
        if item[0] == result[-1][0]:
            result[-1][1] += 1
        else:
            result.append(list(item))
    return [tuple(t) for t in result]

def rle_encode_optimized(s):
    if not s:
        return []
    initial_pairs = [(s[0], 1)] + [(ch, cnt + 1) if ch == prev else (ch, 1) for prev, ch in zip(s, s[1:])]
    return compress_tuples(initial_pairs)

if __name__ == '__main__':
    print(rle_encode_optimized("AAABBBCCDAA"))
    print(rle_encode_optimized("ABCDE"))
    print(rle_encode_optimized("A"))
    print(rle_encode_optimized(""))
    print(rle_encode_optimized("AABBCC"))
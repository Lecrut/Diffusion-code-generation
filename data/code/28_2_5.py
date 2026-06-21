def compress_rle(s):
    if not s:
        return ""
    return "".join(f"{count}{char}" for char, count in (lambda chars: [(k, len(list(g))) for k, g in __import__('itertools').groupby(chars)])(s))

if __name__ == '__main__':
    sample_string = "aaaaaaaaaaabbbbbbbbbccccccccccccddddddddddeeeeeeeeeefffffffffffgggggggggggghhhhhhhhhh"
    result = compress_rle(sample_string)
    print(result)
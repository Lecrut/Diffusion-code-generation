def run_length_encode(s):
    if not s:
        return ""
    return "".join(str(count) + char for char, count in ((k, len(list(g))) for k, g in __import__('itertools').groupby(s)))

def run_length_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        digits = []
        while i < n and s[i].isdigit():
            digits.append(s[i])
            i += 1
        count = int("".join(digits)) if digits else 1
        if i < n:
            char = s[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    original = "AAAABBBCCDAA"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {original == decoded}")
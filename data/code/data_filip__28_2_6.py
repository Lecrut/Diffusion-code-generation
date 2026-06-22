def run_length_encode(s):
    if not s:
        return ""
    encoded = [f"{count}{char}" for char, count in zip(
        (s[i] for i in range(len(s)) if i == 0 or s[i] != s[i-1]),
        (len(list(g)) for k, g in __import__('itertools').groupby(s))
    )]
    return "".join(encoded)

if __name__ == '__main__':
    input_string = "aaabbbcccaaa"
    result = run_length_encode(input_string)
    print(result)
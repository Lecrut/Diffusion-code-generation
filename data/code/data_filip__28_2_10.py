import itertools

def run_length_encode(s):
    result = [[k, len(list(g))] for k, g in itertools.groupby(s)]
    return ''.join(f"{count}{char}" for char, count in result)

if __name__ == '__main__':
    long_string = "AAAAAAABBBCCDAA"
    encoded = run_length_encode(long_string)
    print(encoded)
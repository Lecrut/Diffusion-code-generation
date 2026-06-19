def extract_substrings(S, L):
    substrings = []
    n = len(S)
    for i in range(n - L + 1):
        substrings.append(S[i:i+L])
    return substrings

if __name__ == '__main__':
    S = "abcdefg"
    L = 3
    result = extract_substrings(S, L)
    print(result)
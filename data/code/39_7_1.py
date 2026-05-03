def extract_substrings(S, L):
    n = len(S)
    if L <= 0 or L > n:
        return []
    substrings = []
    for i in range(n - L + 1):
        substrings.append(S[i:i+L])
    return substrings
if __name__ == '__main__':
    S_sample = "abcdefghijk"
    L_sample = 3
    result = extract_substrings(S_sample, L_sample)
    print(result)
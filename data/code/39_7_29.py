def extract_substrings(S, L):
    n = len(S)
    if L <= 0 or L > n:
        return []
    substrings = [S[i:i+L] for i in range(n - L + 1)]
    return substrings

if __name__ == '__main__':
    sample_string = "abcdefghijk"
    substring_length = 3
    result = extract_substrings(sample_string, substring_length)
    print(result)
def extract_substrings(S, L):
    def is_valid_length(length, string_length):
        return length > 0 and length <= string_length

    n = len(S)
    if not is_valid_length(L, n):
        return []

    substrings = []
    for i in range(n - L + 1):
        substrings.append(S[i:i+L])
    
    return substrings

if __name__ == '__main__':
    sample_string = "hello world"
    substring_length = 4
    result = extract_substrings(sample_string, substring_length)
    print(result)
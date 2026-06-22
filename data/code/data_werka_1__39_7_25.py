def extract_substrings(S, L):
    n = len(S)
    if L <= 0 or L > n:
        return []
    
    def get_substring(start_index):
        return S[start_index:start_index + L]
    
    substrings = [get_substring(i) for i in range(n - L + 1)]
    return substrings

if __name__ == '__main__':
    sample_string = "abcdefghij"
    substring_length = 3
    result = extract_substrings(sample_string, substring_length)
    print(result)
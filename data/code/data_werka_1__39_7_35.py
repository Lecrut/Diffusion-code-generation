def extract_substrings(S, L):
    if L <= 0 or L > len(S):
        return []
    
    substrings = [S[i:i+L] for i in range(len(S) - L + 1)]
    return substrings

if __name__ == '__main__':
    sample_string = "hello world"
    substring_length = 5
    result = extract_substrings(sample_string, substring_length)
    print(result)
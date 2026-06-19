def extract_substrings(S, L):
    n = len(S)
    if L <= 0 or L > n:
        return []
    
    substrings = []
    for i in range(n - L + 1):
        substrings.append(S[i:i+L])
    
    return substrings

if __name__ == '__main__':
    sample_data = {
        "string": "abcdefghijk",
        "length": 3
    }
    
    S_sample = sample_data["string"]
    L_sample = sample_data["length"]
    result = extract_substrings(S_sample, L_sample)
    print(result)
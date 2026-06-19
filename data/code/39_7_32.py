def is_valid_length(S, L):
    return 0 < L <= len(S)

def extract_substrings(S, L):
    if not is_valid_length(S, L):
        return []
    substrings = [S[i:i+L] for i in range(len(S) - L + 1)]
    return substrings

if __name__ == '__main__':
    sample_string = "hello_world"
    substring_length = 2
    result = extract_substrings(sample_string, substring_length)
    print(result)
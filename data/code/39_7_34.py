def extract_substrings(S, L):
    n = len(S)
    if L <= 0 or L > n:
        return []
    
    substrings = []
    for start_index in range(n - L + 1):
        end_index = start_index + L
        substring = S[start_index:end_index]
        substrings.append(substring)
    
    return substrings

if __name__ == '__main__':
    sample_string = "xyzabcdefg"
    length_of_substring = 4
    extracted_substrings = extract_substrings(sample_string, length_of_substring)
    print(extracted_substrings)
def find_unique_substrings(s):
    if not isinstance(s, str) or len(s) < 3:
        raise ValueError("Input must be a string with length >= 3")
    
    substrings = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 3, n + 1):
            substrings.add(s[i:j])
    return sorted(substrings)

if __name__ == '__main__':
    sample_string = "abcde"
    print(find_unique_substrings(sample_string))
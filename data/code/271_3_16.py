def find_unique_substrings(s):
    substrings = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 3, n + 1):
            substring = s[i:j]
            if substring not in substrings:
                substrings.add(substring)
    return substrings

if __name__ == '__main__':
    sample_string = "abcde"
    unique_substrings = find_unique_substrings(sample_string)
    print(unique_substrings)
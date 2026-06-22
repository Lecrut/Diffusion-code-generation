def find_unique_substrings(s):
    substrings = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, len(s) + 1):
            substrings.add(s[i:j])
    return sorted(substrings)

if __name__ == '__main__':
    sample_string = "abcde"
    print(find_unique_substrings(sample_string))
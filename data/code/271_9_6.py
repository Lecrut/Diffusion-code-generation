MIN_SUBSTRING_LENGTH = 3

def find_unique_substrings(s):
    substrings = set()
    n = len(s)
    for i in range(n):
        for j in range(i + MIN_SUBSTRING_LENGTH, n + 1):
            substrings.add(s[i:j])
    return sorted(substrings)

if __name__ == '__main__':
    sample_string = "abcde"
    print(find_unique_substrings(sample_string))
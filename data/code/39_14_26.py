def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    SAMPLE_STRING_1 = "abc"
    SAMPLE_STRING_2 = "hello"
    
    substrings_1 = list(generate_substrings(SAMPLE_STRING_1))
    print(substrings_1)
    
    substrings_2 = list(generate_substrings(SAMPLE_STRING_2))
    print(substrings_2)
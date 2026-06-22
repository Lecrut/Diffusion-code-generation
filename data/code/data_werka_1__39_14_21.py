def substring_generator(s):
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    sample_string = "abc"
    for substring in substring_generator(sample_string):
        print(substring)
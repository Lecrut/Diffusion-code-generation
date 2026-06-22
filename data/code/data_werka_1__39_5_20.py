def substring_generator(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]

if __name__ == '__main__':
    sample_string = "abc"
    for substring in substring_generator(sample_string):
        print(substring)
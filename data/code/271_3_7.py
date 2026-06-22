def find_unique_substrings(input_string):
    substrings = set()
    length = len(input_string)
    for start in range(length):
        for end in range(start + 3, length + 1):
            substring = input_string[start:end]
            if len(substring) >= 3:
                substrings.add(substring)
    return substrings

if __name__ == '__main__':
    sample_string = "abcde"
    unique_substrings = find_unique_substrings(sample_string)
    for substring in sorted(unique_substrings):
        print(substring)
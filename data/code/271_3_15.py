def find_unique_substrings(input_string):
    substrings = set()
    n = len(input_string)
    for i in range(n - 2):
        for j in range(3, n - i + 1):
            substring = input_string[i:i+j]
            if substring not in substrings:
                substrings.add(substring)
    return substrings

if __name__ == '__main__':
    sample_string = "abcde123"
    unique_substrings = find_unique_substrings(sample_string)
    print(unique_substrings)
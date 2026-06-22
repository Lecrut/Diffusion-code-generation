def find_unique_substrings(input_string):
    substrings = set()
    n = len(input_string)
    
    for i in range(n - 2):
        for j in range(i + 3, n + 1):
            substring = input_string[i:j]
            if len(substring) >= 3:
                substrings.add(substring)
                
    return substrings

if __name__ == '__main__':
    sample_string = "abcde"
    unique_substrings = find_unique_substrings(sample_string)
    for substring in sorted(unique_substrings):
        print(substring)
def find_unique_substrings(input_string):
    substrings = set()
    length = len(input_string)
    
    for i in range(length - 2):
        for j in range(i + 3, length + 1):
            substring = input_string[i:j]
            if substring not in substrings:
                substrings.add(substring)
                
    return substrings

if __name__ == '__main__':
    sample_string = "abcde"
    unique_substrings = find_unique_substrings(sample_string)
    for substring in sorted(unique_substrings):
        print(f"'{substring}'")
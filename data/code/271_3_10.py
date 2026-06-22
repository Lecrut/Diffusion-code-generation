MIN_SUBSTRING_LENGTH = 3

def find_unique_substrings(input_string):
    substrings = set()
    length = len(input_string)
    
    for start in range(length):
        for end in range(start + MIN_SUBSTRING_LENGTH, length + 1):
            substring = input_string[start:end]
            if len(substring) >= MIN_SUBSTRING_LENGTH:
                substrings.add(substring)
                
    return substrings

if __name__ == '__main__':
    sample_string = "abcde"
    unique_substrings = find_unique_substrings(sample_string)
    print(unique_substrings)
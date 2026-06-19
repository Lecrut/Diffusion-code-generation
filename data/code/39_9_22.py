def find_nested_substrings(phrase):
    nested_substrings = []
    length = len(phrase)
    
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = phrase[i:j]
            if any(substring in s for s in nested_substrings):
                nested_substrings.append(substring)
    
    return nested_substrings

if __name__ == '__main__':
    sample_phrase = "ababa"
    result = find_nested_substrings(sample_phrase)
    print(result)
def find_nested_substrings(phrase):
    nested_substrings = []
    length = len(phrase)
    
    for i in range(length):
        for j in range(i + 1, length + 1):
            nested_substrings.append(phrase[i:j])
    
    return nested_substrings

if __name__ == '__main__':
    sample_phrase = "abc"
    result = find_nested_substrings(sample_phrase)
    print(result)
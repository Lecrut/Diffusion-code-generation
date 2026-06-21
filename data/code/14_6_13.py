def find_unique_characters(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    unique_chars = [char for char, count in freq.items() if count == 1]
    return ''.join(sorted(unique_chars))

if __name__ == '__main__':
    sample_string = "programming"
    result = find_unique_characters(sample_string)
    print(result)
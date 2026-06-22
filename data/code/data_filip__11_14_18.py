def detect_frequency_duplicates(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    
    freq_counts = {}
    for char, count in freq.items():
        if count not in freq_counts:
            freq_counts[count] = []
        freq_counts[count].append(char)
    
    duplicates = {}
    for count, chars in freq_counts.items():
        if len(chars) > 1:
            duplicates[count] = sorted(chars)
    
    return duplicates

if __name__ == '__main__':
    sample_text = "hello world programming python code test duplicate frequency"
    result = detect_frequency_duplicates(sample_text)
    print(result)
def count_character_frequencies(s):
    freqs = {}
    for char in s:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
    return freqs

if __name__ == '__main__':
    sample_string = "hello world"
    print(count_character_frequencies(sample_string))
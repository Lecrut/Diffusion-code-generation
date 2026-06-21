def count_char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

if __name__ == '__main__':
    sample_string = "hello world"
    print(count_char_frequency(sample_string))
def count_char_frequency(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_char_frequency(sample_string)
    print(result)
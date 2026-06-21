from collections import Counter

def char_freq_diff(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    diff_counter = counter1 - counter2
    return dict(diff_counter)

if __name__ == '__main__':
    sample_str1 = "hello"
    sample_str2 = "world"
    result = char_freq_diff(sample_str1, sample_str2)
    print(result)
from collections import Counter

def compare_char_frequencies(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    diff_counter = counter1 - counter2
    return dict(diff_counter)

if __name__ == '__main__':
    sample_str1 = "abcdef"
    sample_str2 = "defghi"
    result = compare_char_frequencies(sample_str1, sample_str2)
    print(result)
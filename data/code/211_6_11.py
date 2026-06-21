from collections import Counter

def compare_char_frequency(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    diff = counter1 - counter2
    return dict(diff)

if __name__ == '__main__':
    sample_str1 = "hello world"
    sample_str2 = "world hello"
    result = compare_char_frequency(sample_str1, sample_str2)
    print(result)
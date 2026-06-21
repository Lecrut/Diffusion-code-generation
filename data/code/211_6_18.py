from collections import Counter

def calculate_char_frequency_diff(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    return dict(counter1 - counter2)

if __name__ == '__main__':
    sample_str1 = "python"
    sample_str2 = "java"
    diff = calculate_char_frequency_diff(sample_str1, sample_str2)
    print(diff)
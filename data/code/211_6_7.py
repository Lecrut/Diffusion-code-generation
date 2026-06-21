from collections import Counter

def calculate_char_frequency_difference(string1, string2):
    counter1 = Counter(string1)
    counter2 = Counter(string2)
    frequency_diff = counter1 - counter2
    return dict(frequency_diff)

if __name__ == '__main__':
    sample_string1 = "python"
    sample_string2 = "java"
    difference_result = calculate_char_frequency_difference(sample_string1, sample_string2)
    print(difference_result)
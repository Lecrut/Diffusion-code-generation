from collections import Counter

def validate_input(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All inputs must be strings.")
    if len(strings) != 2:
        raise ValueError("Exactly two strings are required.")

def compare_char_frequencies(str1, str2):
    validate_input([str1, str2])
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    diff_counter = counter1 - counter2
    return dict(diff_counter)

if __name__ == '__main__':
    sample_str1 = "hello"
    sample_str2 = "world"
    result = compare_char_frequencies(sample_str1, sample_str2)
    print(result)
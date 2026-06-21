from collections import Counter

def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    if not all(char.isalpha() for char in str1 + str2):
        raise ValueError("Strings should only contain alphabetic characters")

def compare_char_frequencies(str1, str2):
    validate_strings(str1, str2)
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    diff_counter = counter1 - counter2
    return dict(diff_counter)

if __name__ == '__main__':
    sample_str1 = "hello"
    sample_str2 = "world"
    result = compare_char_frequencies(sample_str1, sample_str2)
    print(result)
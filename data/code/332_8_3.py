import re
def count_vowels_regex(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
def count_vowels_re(text):
    matches = re.findall(r'[aeiouAEIOU]', text)
    return len(matches)
if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Programming is fun"
    sample_text3 = "AEIOUaeiou123"
    print(f"'{sample_text1}':")
    print(f"Original logic result: {count_vowels_regex(sample_text1)}")
    print(f"Regex result: {count_vowels_re(sample_text1)}\n")
    print(f"'{sample_text2}':")
    print(f"Original logic result: {count_vowels_regex(sample_text2)}")
    print(f"Regex result: {count_vowels_re(sample_text2)}\n")
    print(f"'{sample_text3}':")
    print(f"Original logic result: {count_vowels_regex(sample_text3)}")
    print(f"Regex result: {count_vowels_re(sample_text3)}\n")
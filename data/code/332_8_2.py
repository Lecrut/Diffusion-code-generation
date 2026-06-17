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
    sample_text4 = "Rhythm"
    print(f"'{sample_text1}': {count_vowels_re(sample_text1)}")
    print(f"'{sample_text2}': {count_vowels_re(sample_text2)}")
    print(f"'{sample_text3}': {count_vowels_re(sample_text3)}")
    print(f"'{sample_text4}': {count_vowels_re(sample_text4)}")
import re
def count_vowels_regex(text):
    vowel_pattern = r"[aeiouAEIOU]"
    matches = re.findall(vowel_pattern, text)
    return len(matches)
if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Programming is fun"
    sample_text3 = "AEIOUaeiou123"
    sample_text4 = "Rhythm"
    print(f"'{sample_text1}': {count_vowels_regex(sample_text1)}")
    print(f"'{sample_text2}': {count_vowels_regex(sample_text2)}")
    print(f"'{sample_text3}': {count_vowels_regex(sample_text3)}")
    print(f"'{sample_text4}': {count_vowels_regex(sample_text4)}")
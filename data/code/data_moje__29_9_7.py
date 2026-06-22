VOWELS = "aeiouAEIOU"
VOWEL_COUNT_TABLE = bytes.maketrans(VOWELS, " " * len(VOWELS))

def count_vowels(text):
    return text.translate(VOWEL_COUNT_TABLE).count(" ")

if __name__ == "__main__":
    large_string = "Hello World! This is a test string with many vowels. " * 100000
    vowel_count = count_vowels(large_string)
    print(vowel_count)
import unicodedata

def count_consonants(text):
    vowels = set("aeiouAEIOU")
    consonant_count = 0
    for char in text:
        if not char.isalpha():
            continue
        lower_char = char.lower()
        if lower_char not in vowels:
            consonant_count += 1
    return consonant_count

if __name__ == '__main__':
    sample_string = "Hello World! This is a test: café, naïve, résumé."
    result = count_consonants(sample_string)
    print(result)
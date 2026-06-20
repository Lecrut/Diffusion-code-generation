def count_consonants(text):
    vowels = set("aeiouAEIOU")
    consonant_count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)
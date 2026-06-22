def count_consonants(text: str) -> int:
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char.lower() in 'aeiou':
                continue
            consonant_count += 1
    return consonant_count
if __name__ == '__main__':
    sample_text = 'Hello, 世界! Ñoño café naïve.'
    result = count_consonants(sample_text)
    print(result)
import unicodedata

def count_consonants(text: str) -> int:
    consonant_chars = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = 0
    for char in text:
        if char.isalpha():
            category = unicodedata.category(char)
            if category.startswith('L'):
                normalized_char = unicodedata.normalize('NFD', char)[0]
                if normalized_char in consonant_chars:
                    count += 1
    return count

if __name__ == '__main__':
    sample_text = "Héllo, wörld! Ñoño café"
    result = count_consonants(sample_text)
    print(result)
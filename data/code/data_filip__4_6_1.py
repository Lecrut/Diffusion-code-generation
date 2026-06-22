import unicodedata

def count_consonants(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels and not unicodedata.category(char).startswith('M'):
            if unicodedata.category(char) == 'Ll' or unicodedata.category(char) == 'Lu':
                normalized = unicodedata.normalize('NFD', char)
                base_char = normalized[0] if normalized else char
                if base_char.lower() not in vowels and base_char.isalpha():
                    count += 1
    return count

def is_consonant(char):
    if not char.isalpha():
        return False
    normalized = unicodedata.normalize('NFD', char)
    base_char = normalized[0] if normalized else char
    if base_char.lower() in 'aeiou':
        return False
    return True

def count_consonants_unicode(text):
    return sum(1 for char in text if is_consonant(char))

if __name__ == '__main__':
    sample_string = "Hello World! 123 ñ é ü ö à"
    result = count_consonants_unicode(sample_string)
    print(result)
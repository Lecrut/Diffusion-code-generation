import re
def extract_unique_animals(input_string: str) -> list[str]:
    animals = set()
    words = re.findall(r'\b[a-zA-Z]+\b', input_string.lower())
    for word in words:
        if len(word) > 1 and not any(c.isdigit() or c.isupper() for c in word):
            cleaned_word = ''.join(filter(str.isalpha, word))
            animals.add(cleaned_word.title())
    return sorted(list(animals))
if __name__ == '__main__':
    sample_input = "Lion, lion, LION, tiger, Tiger, cat, CAT"
    result = extract_unique_animals(sample_input)
    print(result)
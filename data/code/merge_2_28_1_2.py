import re
def extract_unique_animals(input_string: str) -> list[str]:
    animals = set()
    words = input_string.split()
    for word in words:
        cleaned_word = re.sub(r'[^a-zA-Z\s]', '', word).strip().lower()
        if not cleaned_word or 'animal' in cleaned_word.lower():
            continue
        title_case_word = cleaned_word.capitalize()
        animals.add(title_case_word)
    return sorted(animals, key=lambda x: (len(x), x.lower()))
if __name__ == '__main__':
    sample_input = "Lion lion LEOPARD leopard tiger TIGER cat CAT Cat"
    result = extract_unique_animals(sample_input)
    print(result)
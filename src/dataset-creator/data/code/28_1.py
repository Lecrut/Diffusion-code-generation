def get_unique_animals(input_string: str) -> list[str]:
    animals = set()
    for word in input_string.split():
        if len(word) > 0 and not any(c.isalpha() for c in word):
            continue
        cleaned_word = ''.join(c.lower() for c in word if c.isalpha())
        if cleaned_word:
            animals.add(cleaned_word.title())
    return list(animals)
if __name__ == '__main__':
    sample_input = "lion, Tiger, LEOPARD, tiger, lion"
    result = get_unique_animals(sample_input)
    print(result)
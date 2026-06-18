import re
def extract_unique_animals(input_string: str) -> list[str]:
    normalized = input_string.lower()
    animal_set = set()
    tokens = re.findall(r'[a-zA-Z]+', normalized)
    for token in tokens:
        if token.isalpha():
            clean_token = ''.join(c.capitalize() for c in token)
            animal_set.add(clean_token.lower())                                        
    return sorted(animal_set, key=str.upper)
if __name__ == '__main__':
    sample_input = "lion, Tiger, LEOPARD, tiger, lion"
    result = extract_unique_animals(sample_input)
    print(result)
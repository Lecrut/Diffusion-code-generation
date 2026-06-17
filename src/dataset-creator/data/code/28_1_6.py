import re
def extract_unique_animals(input_string: str) -> list[str]:
    normalized = input_string.lower()
    animal_set = set()
    tokens = re.findall(r'\b[a-zA-Z]+\b', normalized)
    for token in tokens:
        animal_set.add(token.title())
    return list(animal_set)
if __name__ == '__main__':
    sample_input = "Lion, lion, tiger, TIGER, LEOPARD, leopard"
    result = extract_unique_animals(sample_input)
    print(result)
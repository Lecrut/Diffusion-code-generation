import re
def extract_unique_animals(input_string: str) -> list[str]:
    normalized = input_string.lower()
    animal_set = set()
    for word in re.findall(r'[a-zA-Z]+', normalized):
        if len(word) > 0:
            animal_set.add(word.lower())
    return [animal.capitalize() for animal in sorted(animal_set)]
if __name__ == '__main__':
    sample_input = "Lion, lion, Tiger, tiger, LEOPARD, leopard"
    result = extract_unique_animals(sample_input)
    print(result)
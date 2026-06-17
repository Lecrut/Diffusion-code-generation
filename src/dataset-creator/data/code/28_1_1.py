import re
def process_animal_names(input_string: str) -> list[str]:
    normalized_words = [word.lower() for word in input_string.split()]
    unique_animals = {animal.title() for animal in set(normalized_words)}
    return sorted(unique_animals)
if __name__ == '__main__':
    sample_input = "lion, Tiger, lion, tiger, elephant, Elephant"
    result = process_animal_names(sample_input)
    print(result)
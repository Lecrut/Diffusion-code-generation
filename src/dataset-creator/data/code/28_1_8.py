import re
def extract_unique_animals(text: str) -> list[str]:
    words = re.findall(r'[a-zA-Z]+', text.lower())
    unique_animals = {word.title() for word in words}
    return sorted(unique_animals)
if __name__ == '__main__':
    sample_input = "Tiger, lion, LION, tiger, LEOPARD, leopard"
    result = extract_unique_animals(sample_input)
    print(result)
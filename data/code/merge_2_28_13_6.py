import re
def normalize_name(name: str) -> str:
    return name.strip().lower()
def get_unique_animals(*inputs):
    animals = set()
    for item in inputs:
        if isinstance(item, (list, tuple)):
            for animal in item:
                normalized = normalize_name(animal)
                if not any(normalized == a.lower() for a in animals):
                    animals.add(normalized)
        elif isinstance(item, set):
            for animal in item:
                normalized = normalize_name(animal)
                if not any(normalized == a.lower() for a in animals):
                    animals.add(normalized)
        else:
            normalized = normalize_name(str(item))
            if not any(normalized == a.lower() for a in animals):
                animals.add(normalized)
    return sorted(animals, key=str.upper)
if __name__ == '__main__':
    sample_data_1 = ['Lion', 'Tiger']
    sample_data_2 = {'lion', 'tiger'}
    sample_data_3 = ['elephant', 'Elephant']
    result = get_unique_animals(sample_data_1, sample_data_2, sample_data_3)
    print(result)
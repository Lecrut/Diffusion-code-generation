import collections
def validate_animal(name: str) -> bool:
    VALID_ANIMALS = {"lion", "tiger", "elephant", "giraffe"}
    return name.lower() in VALID_ANIMALS
def deduplicate_animals(entries: list[str]) -> collections.OrderedDict:
    seen = set()
    result = collections.OrderedDict()
    for entry in entries:
        if not isinstance(entry, str):
            continue
        name_lower = entry.lower().strip()
        if validate_animal(name_lower) and name_lower not in seen:
            seen.add(name_lower)
            result[name_lower] = True
    return result
if __name__ == '__main__':
    SAMPLE_ENTRIES = [
        "Lion",
        "tiger",
        "Elephant",
        "giraffe",
        "lion",
        "bear",
        "TIGER"
    ]
    unique_animals = deduplicate_animals(SAMPLE_ENTRIES)
    print("Unique Animals:")
    for animal in unique_animals:
        print(animal)
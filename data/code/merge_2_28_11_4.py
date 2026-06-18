import collections
def validate_animal(entry: str) -> bool:
    ALLOWED_ANIMALS = {"lion", "tiger", "elephant", "giraffe"}
    return entry.lower() in ALLOWED_ANIMALS
def deduplicate_animals(entries: list[str]) -> dict[str, int]:
    seen = set()
    result_order = []
    counts = {}
    for entry in entries:
        if not validate_animal(entry):
            continue
        normalized_entry = entry.lower().strip()
        if normalized_entry not in seen:
            seen.add(normalized_entry)
            result_order.append(normalized_entry)
            counts[normalized_entry] = 1
        else:
            counts[normalized_entry] += 1
    return collections.OrderedDict(zip(result_order, [counts[k] for k in result_order]))
if __name__ == '__main__':
    SAMPLE_DATA = ["Lion", "tiger", "elephant", "giraffe", "lion", "Tiger", "invalid_entry"]
    unique_animals = deduplicate_animals(SAMPLE_DATA)
    print("Unique Animals and Counts:")
    for animal, count in unique_animals.items():
        print(f"{animal}: {count}")
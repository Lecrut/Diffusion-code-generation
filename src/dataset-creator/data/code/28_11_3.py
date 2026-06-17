from collections import OrderedDict
def is_valid_animal(entry: str) -> bool:
    VALID_ANIMALS = {
        "dog", "cat", "bird", "fish", "rabbit", "horse", "cow", "pig", "goat", "sheep"
    }
    return entry.lower().strip() in VALID_ANIMALS
def deduplicate_animals(entries: list[str]) -> OrderedDict[str, None]:
    result = OrderedDict()
    for index, entry in enumerate(entries):
        if not isinstance(entry, str) or not entry.strip():
            raise ValueError(f"Invalid entry at index {index}: '{entry}'")
        cleaned_entry = entry.lower().strip()
        if is_valid_animal(cleaned_entry):
            result[cleaned_entry] = None
        else:
            raise ValueError(
                f"Entry at index {index} rejected as invalid animal: '{cleaned_entry}'. "
                "Valid animals are limited to dog, cat, bird, fish, rabbit, horse, cow, pig, goat, and sheep."
            )
    return result
if __name__ == '__main__':
    sample_data = [
        "Dog",
        "cat",
        "Bird",
        "dog",
        "Fish",
        "Rabbit",
        "Invalid entry here",
        "",
        "Horse"
    ]
    try:
        unique_animals = deduplicate_animals(sample_data)
        print("Deduplicated animals:", list(unique_animals.keys()))
    except ValueError as e:
        print(f"Validation error encountered: {e}")
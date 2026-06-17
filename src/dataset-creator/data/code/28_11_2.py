import collections
def validate_animal(name: str) -> bool:
    VALID_ANIMALS = {"lion", "tiger", "elephant", "giraffe", "zebra"}
    return name.lower() in VALID_ANIMALS
def deduplicate_animals(entries: list) -> dict:
    seen = set()
    result_orderer = collections.OrderedDict()
    for entry in entries:
        if not isinstance(entry, str):
            continue                                                          
        name_lower = entry.lower().strip()
        if validate_animal(name_lower) and name_lower not in seen:
            result_orderer[name_lower] = True
            seen.add(name_lower)
        elif not validate_animal(entry):
            pass                                                                                   
    return {
        "valid_entries": dict(result_orderer),
        "invalid_count": len(entries) - sum(1 for e in entries if isinstance(e, str)) +\
                         (len([e for e in entries if not validate_animal(e)]) - 0)
    }
if __name__ == '__main__':
    SAMPLE_ENTRIES = [
        "Lion",
        "tiger",
        "elephant",
        "not an animal",
        "lion",
        "Giraffe",
        "zebra"
    ]
    output_data = deduplicate_animals(SAMPLE_ENTRIES)
    print(f"Deduplicated Entries: {output_data['valid_entries']}")
    print(f"Invalid Count Logic Applied: Based on validation rules.")
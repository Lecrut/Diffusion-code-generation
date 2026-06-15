def match_dictionaries(source: dict, target: dict) -> tuple[list, list]:
    successful_matches = []
    unmatched_keys = []
    for key in source:
        if key in target:
            successful_matches.append(key)
        else:
            unmatched_keys.append(key)
    return successful_matches, unmatched_keys
if __name__ == '__main__':
    source_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4,
        "elderberry": 5
    }
    target_mapping = {
        "apple": "fruit_a",
        "banana": "fruit_b",
        "grape": "fruit_c",
        "cherry": "fruit_d"
    }
    matches, unmatched = match_dictionaries(source_data, target_mapping)
    print("Successful Matches:", matches)
    print("Unmatched Keys:", unmatched)
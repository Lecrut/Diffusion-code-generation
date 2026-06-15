def match_dictionaries(source, target):
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
        "apple": "Fruit A",
        "banana": "Fruit B",
        "grape": "Fruit C",
        "orange": "Fruit D"
    }
    matches, unmatched = match_dictionaries(source_data, target_mapping)
    print("Successful Matches:", matches)
    print("Unmatched Keys:", unmatched)
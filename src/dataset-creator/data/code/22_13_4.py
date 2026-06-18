def match_dictionaries(source_dict, target_mapping):
    successful_matches = []
    unmatched_keys = []
    for key in source_dict:
        if key in target_mapping:
            successful_matches.append(key)
        else:
            unmatched_keys.append(key)
    return successful_matches, unmatched_keys
if __name__ == '__main__':
    source = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    target = {
        "apple": "fruit",
        "banana": "fruit",
        "grape": "fruit"
    }
    matches, unmatched = match_dictionaries(source, target)
    print("Successful Matches:", matches)
    print("Unmatched Keys:", unmatched)
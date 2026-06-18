def group_fruits(fruit_list):
    groups = {}
    for fruit in fruit_list:
        if fruit not in groups:
            groups[fruit] = []
        groups[fruit].append(fruit)
    return groups
if __name__ == '__main__':
    sample_data = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]
    expected_output = {
        "apple": ["apple", "apple", "apple"],
        "banana": ["banana", "banana"],
        "orange": ["orange"],
        "grape": ["grape"]
    }
    actual_output = group_fruits(sample_data)
    assert actual_output == expected_output
    print("Test passed!")
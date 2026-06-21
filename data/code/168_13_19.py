LENGTH_GROUPS = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: []
}

def group_by_length(items):
    for item in items:
        length = len(item)
        if length in LENGTH_GROUPS:
            LENGTH_GROUPS[length].append(item)
    return LENGTH_GROUPS

if __name__ == '__main__':
    sample_values = ["hi", "hello", "hey", "welcome", "goodbye", "yo"]
    result = group_by_length(sample_values)
    for key, value in sorted(result.items()):
        print(f"{key}: {value}")
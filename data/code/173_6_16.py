def group_data(data, key_func):
    groups = {}
    for item in data:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

def group_generator(data, key_func):
    groups = {}
    for item in data:
        key = key_func(item)
        if key not in groups:
            yield key
            groups[key] = []
        groups[key].append(item)

if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]

    def key_func(line):
        return line.split(',')[2].strip()

    grouped_data = group_data(sample_data, key_func)
    print(grouped_data)

    print("\nGenerator output:")
    for group in group_generator(sample_data, key_func):
        print(f"Group: {group}")
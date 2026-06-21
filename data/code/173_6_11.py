def group_data(data_iterable, key_func):
    groups = {}
    for item in data_iterable:
        if not item.strip():
            continue
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

def create_group_generator(data_iterable, key_func):
    def group_generator():
        groups = {}
        for item in data_iterable:
            if not item.strip():
                continue
            key = key_func(item)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
            yield groups.copy()
    return group_generator

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

    grouped_generator = create_group_generator(sample_data, key_func)
    for groups in grouped_generator():
        print(groups)
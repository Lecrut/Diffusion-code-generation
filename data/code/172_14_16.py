def create_noun_mapping():
    return {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }

if __name__ == '__main__':
    noun_map = create_noun_mapping()
    print("Noun Mapping:")
    for key in sorted(noun_map.keys()):
        print(f"{key}: {noun_map[key]}")
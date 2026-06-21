def validate_input(input_data):
    if not isinstance(input_data, dict):
        raise ValueError("Input must be a dictionary")
    if not all(isinstance(k, int) for k in input_data.keys()):
        raise ValueError("All keys must be integers")
    if not all(isinstance(v, str) and len(v.split()) == 1 for v in input_data.values()):
        raise ValueError("All values must be simple nouns as single words")

def create_noun_mapping(input_data):
    validate_input(input_data)
    return {key: value for key, value in input_data.items()}

if __name__ == '__main__':
    noun_pairs = {
        1: 'apple',
        2: 'banana',
        3: 'cherry',
        4: 'date'
    }
    noun_map = create_noun_mapping(noun_pairs)
    print("Noun Mapping:")
    for key, word in noun_map.items():
        print(f"{key}: {word}")
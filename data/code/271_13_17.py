CHAR_TYPES = {
    'uppercase': str.isupper,
    'lowercase': str.islower,
    'digits': str.isdigit,
    'special': lambda char: not any(char_type(char) for char_type in CHAR_TYPES.values())
}

def count_character_types(input_file, output_file):
    counts = {key: 0 for key in CHAR_TYPES}
    with open(input_file, 'r') as file:
        content = file.read()
        for char in content:
            for char_type, check_func in CHAR_TYPES.items():
                if check_func(char):
                    counts[char_type] += 1
    with open(output_file, 'w') as file:
        for key, value in counts.items():
            file.write(f'{key}: {value}\n')

if __name__ == '__main__':
    count_character_types('sample.txt', 'output.txt')
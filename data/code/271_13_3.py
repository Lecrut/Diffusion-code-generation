def count_character_types(input_file, output_file):
    counts = {'uppercase': 0, 'lowercase': 0, 'digits': 0, 'special': 0}
    
    with open(input_file, 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    counts['uppercase'] += 1
                elif char.islower():
                    counts['lowercase'] += 1
                elif char.isdigit():
                    counts['digits'] += 1
                else:
                    counts['special'] += 1
    
    with open(output_file, 'w') as file:
        for key, value in counts.items():
            file.write(f'{key}: {value}\n')

if __name__ == '__main__':
    try:
        count_character_types('sample.txt', 'output.txt')
    except Exception as e:
        print(f"Error: {e}")
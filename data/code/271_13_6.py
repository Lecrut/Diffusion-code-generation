def count_character_types(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    
    counts = {
        'uppercase': sum(1 for char in content if char.isupper()),
        'lowercase': sum(1 for char in content if char.islower()),
        'digits': sum(1 for char in content if char.isdigit()),
        'special': sum(1 for char in content if not char.isalnum())
    }
    
    with open(output_file, 'w') as file:
        for key, value in counts.items():
            file.write(f'{key}: {value}\n')

if __name__ == '__main__':
    count_character_types('sample.txt', 'output.txt')
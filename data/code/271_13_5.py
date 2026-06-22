def is_uppercase(char):
    return char.isupper()

def is_lowercase(char):
    return char.islower()

def is_digit(char):
    return char.isdigit()

def is_special(char):
    return not any([is_uppercase(char), is_lowercase(char), is_digit(char)])

def count_character_types(input_file, output_file):
    counts = {'uppercase': 0, 'lowercase': 0, 'digits': 0, 'special': 0}
    
    with open(input_file, 'r') as file:
        for line in file:
            for char in line:
                if is_uppercase(char):
                    counts['uppercase'] += 1
                elif is_lowercase(char):
                    counts['lowercase'] += 1
                elif is_digit(char):
                    counts['digits'] += 1
                else:
                    counts['special'] += 1
    
    with open(output_file, 'w') as file:
        for key, value in counts.items():
            file.write(f'{key}: {value}\n')

if __name__ == '__main__':
    count_character_types('sample.txt', 'output.txt')
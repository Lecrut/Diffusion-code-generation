class CharacterCounter:
    CHAR_TYPES = {
        'uppercase': str.isupper,
        'lowercase': str.islower,
        'digits': str.isdigit,
        'special': lambda char: not any(char_type(char) for char_type in CHAR_TYPES.values())
    }
    
    def __init__(self, input_file):
        self.input_file = input_file
        self.counts = {key: 0 for key in self.CHAR_TYPES}
    
    @staticmethod
    def count_characters(input_file):
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
        return counts
    
    def write_counts_to_file(self, output_file):
        with open(output_file, 'w') as file:
            for key, value in self.counts.items():
                file.write(f'{key}: {value}\n')

if __name__ == '__main__':
    counter = CharacterCounter('sample.txt')
    counts = CharacterCounter.count_characters('sample.txt')
    counter.write_counts_to_file('output.txt')
    print(counts)
class CharacterCounter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.counts = {'uppercase': 0, 'lowercase': 0, 'digits': 0, 'special': 0}

    def count_characters(self):
        with open(self.input_file, 'r') as file:
            for line in file:
                for char in line:
                    if char.isupper():
                        self.counts['uppercase'] += 1
                    elif char.islower():
                        self.counts['lowercase'] += 1
                    elif char.isdigit():
                        self.counts['digits'] += 1
                    else:
                        self.counts['special'] += 1

    def write_counts_to_file(self, output_file):
        with open(output_file, 'w') as file:
            for key, value in self.counts.items():
                file.write(f'{key}: {value}\n')

if __name__ == '__main__':
    counter = CharacterCounter('sample.txt')
    counter.count_characters()
    counter.write_counts_to_file('output.txt')
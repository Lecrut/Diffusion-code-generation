class InstructionRepeater:
    def __init__(self):
        self.instructions = []

    def load_instructions(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.instructions = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")

    def repeat_instructions(self, count=3):
        for instruction in self.instructions:
            print(instruction)
            for _ in range(count - 1):
                print(instruction)

if __name__ == '__main__':
    repeater = InstructionRepeater()
    sample_content = [
        "Instruction one",
        "Instruction two",
        "Instruction three"
    ]
    with open('instructions.txt', 'w') as f:
        for line in sample_content:
            f.write(line + '\n')
    
    repeater.load_instructions('instructions.txt')
    repeater.repeat_instructions(3)
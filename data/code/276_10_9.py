class InstructionRepeater:
    REPEAT_COUNT = 3

    @staticmethod
    def read_instructions(filepath):
        try:
            with open(filepath, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            return []

    def repeat_instructions(self, filepath):
        instructions = self.read_instructions(filepath)
        for instruction in instructions:
            for _ in range(self.REPEAT_COUNT):
                print(instruction)

if __name__ == '__main__':
    repeater = InstructionRepeater()
    sample_content = [
        "Instruction one",
        "Instruction two",
        "Instruction three"
    ]
    with open("instructions.txt", 'w') as f:
        for line in sample_content:
            f.write(line + '\n')
    repeater.repeat_instructions("instructions.txt")
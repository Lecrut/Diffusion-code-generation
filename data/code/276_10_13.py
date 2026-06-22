class InstructionRepeater:
    def __init__(self):
        self.sample_instructions = [
            "Instruction one",
            "Instruction two",
            "Instruction three"
        ]

    def repeat_instruction(self, instruction, times):
        for _ in range(times):
            print(instruction)

    def execute_repetitions(self):
        for instruction in self.sample_instructions:
            self.repeat_instruction(instruction, 3)

if __name__ == '__main__':
    repeater = InstructionRepeater()
    repeater.execute_repetitions()
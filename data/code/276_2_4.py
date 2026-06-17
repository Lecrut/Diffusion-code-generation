class InstructionSequence:
    def __init__(self):
        self.instructions = []
    def add_instruction(self, instruction):
        self.instructions.append(instruction)
    def repeat_instruction(self, instruction, times):
        for _ in range(times):
            self.add_instruction(instruction)
    def get_sequence(self):
        return self.instructions
if __name__ == '__main__':
    seq = InstructionSequence()
    seq.add_instruction("Move forward")
    seq.repeat_instruction("Turn right", 3)
    seq.add_instruction("Jump")
    seq.repeat_instruction("Move forward", 2)
    final_sequence = seq.get_sequence()
    for instruction in final_sequence:
        print(instruction)
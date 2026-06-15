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
    sequence_manager = InstructionSequence()
    sequence_manager.add_instruction("Move forward")
    sequence_manager.add_instruction("Turn left")
    sequence_manager.repeat_instruction("Move forward", 3)
    sequence_manager.repeat_instruction("Turn left", 2)
    sequence_manager.repeat_instruction("Move forward", 1)
    final_sequence = sequence_manager.get_sequence()
    print("Instruction Sequence:")
    for instruction in final_sequence:
        print(instruction)
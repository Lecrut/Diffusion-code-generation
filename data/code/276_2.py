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
    sequence_manager.add_instruction("Move Forward")
    sequence_manager.add_instruction("Turn Right")
    sequence_manager.repeat_instruction("Move Forward", 3)
    sequence_manager.repeat_instruction("Turn Right", 1)
    sequence_manager.repeat_instruction("Move Forward", 2)
    final_sequence = sequence_manager.get_sequence()
    for instruction in final_sequence:
        print(instruction)
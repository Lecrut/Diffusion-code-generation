class InstructionSequence:
    def __init__(self):
        self.instructions = []
    def add_instruction(self, instruction):
        self.instructions.append(instruction)
    def repeat_instruction(self, index, count):
        if 0 <= index < len(self.instructions):
            for _ in range(count):
                self.instructions.insert(index, self.instructions[index])
        else:
            raise IndexError("Instruction index out of bounds")
    def display_sequence(self):
        return self.instructions
if __name__ == '__main__':
    sequence_manager = InstructionSequence()
    sequence_manager.add_instruction("Move Forward")
    sequence_manager.add_instruction("Turn Right")
    sequence_manager.add_instruction("Move Forward")
    print("Initial Sequence:")
    print(sequence_manager.display_sequence())
    sequence_manager.repeat_instruction(1, 2)
    print("\nSequence after repeating 'Turn Right' twice at index 1:")
    print(sequence_manager.display_sequence())
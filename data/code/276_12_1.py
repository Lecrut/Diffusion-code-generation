class InstructionRepeater:
    def repeat_instructions(self, instructions, repetition_factor):
        repeated_instructions = []
        for instruction in instructions:
            repeated_instructions.extend([instruction] * repetition_factor)
        return repeated_instructions
if __name__ == '__main__':
    repeater = InstructionRepeater()
    sample_instructions = ["move forward", "turn left", "jump"]
    repetition = 3
    result = repeater.repeat_instructions(sample_instructions, repetition)
    print(result)
def repeat_instructions(instructions, repetitions):
    for instruction in instructions:
        for _ in range(repetitions):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = [
        "Instruction one",
        "Instruction two",
        "Instruction three"
    ]
    repeat_instructions(sample_instructions, 3)
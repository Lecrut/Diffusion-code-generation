def repeat_instructions(instructions, count):
    for instruction in instructions:
        for _ in range(count):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = [
        "Instruction one",
        "Instruction two",
        "Instruction three"
    ]
    repeat_instructions(sample_instructions, 3)
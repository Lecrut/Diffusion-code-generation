MAX_REPETITIONS = 3

def repeat_instructions(instructions):
    for instruction in instructions:
        for _ in range(MAX_REPETITIONS):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = [
        "Instruction one",
        "Instruction two",
        "Instruction three"
    ]
    repeat_instructions(sample_instructions)
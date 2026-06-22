def repeat_instructions(instructions, repetitions):
    for instruction in instructions:
        if not isinstance(instruction, str) or not instruction.strip():
            raise ValueError("All instructions must be non-empty strings.")
        print(instruction)
        for _ in range(repetitions - 1):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = [
        "Start",
        "Execute step one",
        "Execute step two"
    ]
    repeat_instructions(sample_instructions, 3)
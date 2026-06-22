def repeat_instructions(instructions, repeat_count):
    for instruction in instructions:
        for _ in range(repeat_count):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = [
        "Initialize system",
        "Check sensors",
        "Adjust settings"
    ]
    repeat_instructions(sample_instructions, 2)
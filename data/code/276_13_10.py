def execute_instructions(instructions):
    for instruction, count in instructions.items():
        for _ in range(count):
            exec(instruction)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 4,
        'print("World")': 3
    }
    execute_instructions(sample_instructions)
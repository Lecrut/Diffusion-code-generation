def execute_instructions(instructions):
    for instruction, count in instructions.items():
        exec(instruction * count)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'print("World")': 2
    }
    execute_instructions(sample_instructions)
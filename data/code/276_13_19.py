def execute_instructions(instructions):
    for instruction, count in instructions.items():
        for _ in range(count):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = {
        "print('Hello')": 3,
        "print('World')": 2
    }
    execute_instructions(sample_instructions)
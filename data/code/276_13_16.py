def execute_instructions(instructions):
    for instruction, count in instructions.items():
        for _ in range(count):
            eval(instruction)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'x += 1': 5
    }
    x = 0
    execute_instructions(sample_instructions)
    print(f'Final value of x: {x}')
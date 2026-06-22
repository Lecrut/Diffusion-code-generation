MAX_EXECUTION_COUNT = 10

def execute_instruction(instruction):
    try:
        exec(instruction)
    except Exception as e:
        print(f"Error executing {instruction}: {e}")

def execute_instructions(instructions):
    for instruction, count in instructions.items():
        if count > MAX_EXECUTION_COUNT:
            print(f"Skipping {instruction} due to excessive repeat count")
            continue
        for _ in range(count):
            execute_instruction(instruction)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'print("World")': 2,
        '1 / 0': 1
    }
    execute_instructions(sample_instructions)
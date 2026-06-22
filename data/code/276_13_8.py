def validate_instructions(instructions):
    if not isinstance(instructions, dict):
        raise ValueError("Instructions must be a dictionary")
    for instruction, count in instructions.items():
        if not isinstance(instruction, str) or not isinstance(count, int):
            raise ValueError("Invalid instruction format")

def execute_instruction(instruction, count):
    for _ in range(count):
        exec(instruction)

def execute_instructions(instructions):
    validate_instructions(instructions)
    for instruction, count in instructions.items():
        execute_instruction(instruction, count)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'print("World")': 2
    }
    execute_instructions(sample_instructions)
def execute_instructions(instructions):
    for instruction, count in instructions.items():
        if not isinstance(instruction, str) or not isinstance(count, int) or count < 0:
            raise ValueError(f"Invalid instruction: {instruction} or count: {count}")
        exec_block = f"""
def run_instruction():
    for _ in range({count}):
        {instruction}
run_instruction()
"""
        exec(exec_block)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'print("World")': 2
    }
    execute_instructions(sample_instructions)
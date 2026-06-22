def execute_instructions(instructions):
    for instruction, count in instructions.items():
        for _ in range(count):
            try:
                exec(instruction)
            except Exception as e:
                print(f"Error executing {instruction}: {e}")

if __name__ == '__main__':
    sample_instructions = {
        'print("Python")': 2,
        'print(42)': 1
    }
    execute_instructions(sample_instructions)
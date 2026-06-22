def execute_instructions(instructions):
    for instruction, count in instructions.items():
        try:
            exec(instruction)
        except Exception as e:
            print(f"Error executing {instruction}: {e}")

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'print("World")': 2
    }
    execute_instructions(sample_instructions)